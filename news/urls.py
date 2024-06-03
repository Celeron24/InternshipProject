from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('entertainment_and_arts/', views.entertainment_and_arts, name='entertainment_and_arts'),
    path('health/', views.health, name='health'),
    path('business/', views.business, name='business'),
    path('asia/', views.asia, name='asia'),
    path('africa/', views.africa, name='africa'),
    path('europe/', views.europe, name='europe'),
    path('middleeast/', views.middle_east, name='middleeast'),
    path('us&canada/', views.us_canada, name='us&canada'),
    path('england/', views.england, name='england'),
    path('northernireland/', views.northern_ireland, name='northernireland'),
    path('scotland/', views.scotland, name='scotland'),
    path('wales/', views.wales, name='wales'),
    path('politics/', views.politics, name='politics'),
    path('sports/', views.sports, name='sports'),
    path('business/', views.business, name='business'),
    path('technology/', views.technology, name='technology'),
    path('LatinAmerica/', views.latin_america, name='LatinAmerica'),
    path('search/', views.rss_feed_search, name='rss_feed_search'),

]
