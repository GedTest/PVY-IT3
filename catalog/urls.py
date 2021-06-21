from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.index, name='index'),

    # urls for BRICK
    path('brick/<int:pk>/', views.BrickDetailView.as_view(), name='brick-detail'),
    path('bricks/', views.BrickListView.as_view(), name='brick_list'),
    path('brick/<int:pk>/update/', views.BrickUpdateView.as_view(), name='brick_update'),
    path('brick/<int:pk>/delete/', views.BrickDeleteView.as_view(), name='brick_delete'),
    path('brick/create/', views.BrickCreateView.as_view(), name='brick_create'),

    # urls for MANUALS
    path('manual/<int:pk>/', views.ManualDetailView.as_view(), name='manual-detail'),
    path('manuals/', views.ManualListView.as_view(), name='manual_list'),
    path('manual/<int:pk>/update/', views.ManualUpdateView.as_view(), name='manual_update'),
    path('manual/<int:pk>/delete/', views.ManualDeleteView.as_view(), name='manual_delete'),
    path('manual/create/', views.ManualCreateView.as_view(), name='manual_create'),

    # urls for SETS
    path('set/<int:pk>/', views.SetDetailView.as_view(), name='set-detail'),
    path('sets/', views.SetListView.as_view(), name='set_list'),
    path('set/<int:pk>/update/', views.SetUpdateView.as_view(), name='set_update'),
    path('set/<int:pk>/delete/', views.SetDeleteView.as_view(), name='set_delete'),
    path('set/create/', views.SetCreateView.as_view(), name='set_create'),
   ]
