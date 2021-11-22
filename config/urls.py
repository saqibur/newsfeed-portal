from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('archon/', admin.site.urls),
    url('user/', include('users.urls', namespace='user')),
]
