"""
Website app urlconfig
"""
from django.urls import path
from django.views.generic import TemplateView

from website import views

urlpatterns = [
    path('kontakti/', TemplateView.as_view(template_name='website/contacts.html'), name='contacts'),
    path('cenas/', TemplateView.as_view(template_name='website/prices.html'), name='prices'),

    path('jaunumi/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('jaunumi/', views.NewsListView.as_view(), name='news_index'),

    path('ipasibas/<slug:slug>/', views.FeatureDetailView.as_view(), name='feature'),

    path('', views.FrontPage.as_view(), name='front'),
]
