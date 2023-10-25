from django.urls import path, re_path
from apps.authentication.services.auth_token import CustomTokenObtainPairView
from . import views

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(),name="login-v1"),
    path('conta', views.AccountView.as_view(), name='account'),
    re_path(r'^account/(?P<id>\d+)?$', views.AccountView.as_view(), name='account-item'),
    path('contato', views.ContatosView.as_view(), name='contato'),
    re_path(r'^contato/(?P<id>\d+)?$', views.ContatosView.as_view(), name='contato-item'),
]
