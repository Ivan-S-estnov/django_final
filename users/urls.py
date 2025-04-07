from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import *


app_name = UsersConfig.name

urlpatterns = [
                  path('login/', LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', LogoutView.as_view(next_page='mailings:home'), name='logout'),
                  path('register/', UserCreateView.as_view(), name='register'),
                  path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
                  path('users-list/', UserListView.as_view(), name='users_list'),
                  path("profile/<str:email>/block", view=UserBlockView.as_view(), name="profile-block"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)