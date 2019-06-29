from django.urls import path

from . import views

urlpatterns = [
    path('', views.BreedListView.as_view(), name='breeds-list'),
    path('<int:pk>/', views.BreedDetailsView.as_view(), name='breed-details'),
    path('new/', views.BreedCreate.as_view(), name='breed-new'),
]
