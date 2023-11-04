from django.urls import path
from .views import *


app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit-profile/<int:pk>', EditProfileView.as_view(), name='profile'),
]
