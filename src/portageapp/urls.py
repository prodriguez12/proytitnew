"""portageapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from input.views import input_new_view, input_single_view, input_list_view
from output.views import output_single_view
from pages.views import home_view, apply_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'users/', include('users.urls')),
    url(r'users/', include('django.contrib.auth.urls')),
    url(r'input/<int:input_id>/', input_single_view, name = 'input'),
    url(r'inputs/', input_list_view, name = 'inputs'),
    url(r'input/new', input_new_view, name = 'inputnew'),
    url(r'output/<int:output_id>/', output_single_view, name = 'output'),
    url(r'apply/<int:input_id>', apply_view, name='process'),
    url(r'', home_view, name='home'),
]
