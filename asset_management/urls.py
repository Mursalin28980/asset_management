from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.user_login, name='user_login'),
    path('assigned-assets/', views.assigned_assets, name='assigned_assets'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
]