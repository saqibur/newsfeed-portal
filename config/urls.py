from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('archon/', admin.site.urls),
    url(r'users/', include('users.urls', namespace='users')),
]
