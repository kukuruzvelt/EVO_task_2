from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('new_user', views.new_user, name='new_user'),
    path('existing_user', views.existing_user, name='existing_user'),
    path('all_users', views.all_users, name="all_users")
]
