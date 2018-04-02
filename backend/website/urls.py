"""backend URL Configuration
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
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
