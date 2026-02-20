"""healthapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from apps.healthbook.views import healthbook

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name='home/index.html')),
    path(r'articles/', TemplateView.as_view(template_name='home/articles.html')),
    path(r'aboutus/', TemplateView.as_view(template_name='home/aboutus.html')),
    path(r'guidance/', TemplateView.as_view(template_name='home/guidance.html')),
    path(r'term-and-privacy-policy/', TemplateView.as_view(template_name='home/term.html')),
    path(r'contact/', healthbook.contact, name='contact'),
    path(r'feedback/', healthbook.feedback, name='feedback'),
    path('healthbook/', include('apps.healthbook.urls')),
    path('visualization/', include('apps.visualization.urls')),
    path('healthtracker/', include('apps.healthtracker.urls')),
]
