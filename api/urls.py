from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('<int:id>', views.getItem),
    path('update/<int:id>', views.updateItem),
    path('delete/<int:id>', views.deleteItem),
]