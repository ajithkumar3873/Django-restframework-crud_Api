from django.urls import path
from .views import *

urlpatterns = [
    path('products/add/', ProductsView.as_view()),
    path('products/', ProductsView.as_view()),

    path('products/<int:id>/', ProductsViewById.as_view()),
]