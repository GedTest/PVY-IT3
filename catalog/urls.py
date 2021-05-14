from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brick/<int:pk>/', views.BrickDetailView.as_view(), name='brick_detail'),
    path('bricks/', views.BrickListView.as_view(), name='brick_list'),
]
