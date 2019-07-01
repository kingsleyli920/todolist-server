from django.conf.urls import url
from . import views

urlpatterns = [
    url('signup/', views.UsersSignUp.as_view()),
    url('login/', views.UsersLogin.as_view())
]
