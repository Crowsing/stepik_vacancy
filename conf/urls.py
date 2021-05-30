"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path

from vacancy.views import cat_view, companies_view, vacancy_view, main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_view'),
    path('vacancies/cat/<str:vacancies_cat>/', cat_view, name='cat_view'),
    path('companies/<int:company_id>/', companies_view, name='companies_view'),
    re_path(r'^vacancies/?(?P<vacancy_id>\d*)?/$', vacancy_view, name='vacancy_view')
]
