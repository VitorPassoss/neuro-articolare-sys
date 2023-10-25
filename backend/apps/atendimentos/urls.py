from django.urls import path, re_path
from apps.authentication.services.auth_token import CustomTokenObtainPairView
from . import views

urlpatterns = [
    path('sala', views.SalaView.as_view(), name='sala'),
    re_path(r'^sala/(?P<id>\d+)?$', views.SalaView.as_view(), name='sala-item'),
    path('convenio', views.ConvenioView.as_view(), name='convenio'),
    re_path(r'^convenio/(?P<id>\d+)?$', views.ConvenioView.as_view(), name='convenio-item'),
    path('area', views.AreaView.as_view(), name='area'),
    re_path(r'^area/(?P<id>\d+)?$', views.AreaView.as_view(), name='area-item'),
     path('procedimento', views.ProcedimentoView.as_view(), name='procedimentos'),
    re_path(r'^procedimentos/(?P<id>\d+)?$', views.ProcedimentoView.as_view(), name='procedimentos-item'),
    path('atendimento', views.AtendimentoView.as_view(), name='atendimento'),
    re_path(r'^atendimento/(?P<id>\d+)?$', views.AtendimentoView.as_view(), name='atendimento-item'),
]
