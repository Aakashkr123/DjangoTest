# -*- coding: utf-8 -*-
"""
Create on 2016/1/20

@Author:MinRui

@Module Description:
"""
from django.conf.urls import patterns, url
from rango import views

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^about/', views.about, name='about')]
