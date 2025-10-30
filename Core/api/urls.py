from django.contrib import admin
from django.urls import path
from .views import DrawingListView, PriceListView

urlpatterns = [
    path('drawings/', DrawingListView.as_view(), name='Drawing-list'),
    path('prices/', PriceListView.as_view(), name='Price-list'),
]
