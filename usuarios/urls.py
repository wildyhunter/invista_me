from django.urls import path
from .views import CustomLogoutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]