from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipient.urls', namespace='recipient')),
    path('', include('message.urls', namespace='message')),
    path('', include('mailings.urls', namespace='mailings')),
    path('users/', include('users.urls', namespace='users')),
]
