from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items', views.items, name='items'),
    path('loja/<str:pk>', views.loja_items, name='loja_items')
]