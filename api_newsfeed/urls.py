from django.urls import path

from api_newsfeed.views import NewsfeedList

app_name: str = 'api_newsfeed'

urlpatterns = [
    path('newsfeed/', NewsfeedList.as_view(), name='newsfeed'),
]
