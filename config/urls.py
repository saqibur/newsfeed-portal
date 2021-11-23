from django.conf.urls import (
    include,
    url,
)
from django.contrib import admin
from django.urls import path

from config.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('archon/', admin.site.urls),
    url('user/', include('users.urls', namespace='user')),
]
