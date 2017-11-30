from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^ajax/init/', views.init, name='init'),
        url(r'^ajax/requestOdds/', views.requestOdds, name='requestOdds'),
        ]
