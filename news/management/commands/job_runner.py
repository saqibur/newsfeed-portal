from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from news.scheduled_jobs.news_jobs import (
    fetch_top_headlines_job,
    update_sources_job,
)


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
  DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
  def handle(self, *args, **options):
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
      fetch_top_headlines_job,
      trigger          = CronTrigger(minute="*/1"),
      id               = "fetch_top_headlines_job",
      max_instances    = 1,
      replace_existing = True,
    )

    scheduler.add_job(
      update_sources_job,
      trigger          = CronTrigger(minute="*/1"),
      id               = "update_sources_job",
      max_instances    = 1,
      replace_existing = True,
    )

    scheduler.add_job(
      delete_old_job_executions,
      trigger          = CronTrigger(day_of_week="mon", hour="00", minute="00"),
      id               = "delete_old_job_executions",
      max_instances    = 1,
      replace_existing = True,
    )


    try:
      print("Scheduler started")
      scheduler.start()
    except KeyboardInterrupt:
      scheduler.shutdown()
      print("Scheduler stopped")
      exit()
