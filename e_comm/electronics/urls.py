from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('404', TemplateView.as_view(template_name='404.html')),
        path('laptops', views.laptops_list, name='laptops'),
        path('laptops/<str:no>/', views.get_laptops, name='get_laptops'),
        ]
