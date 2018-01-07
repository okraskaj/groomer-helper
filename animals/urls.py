from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnimalListView.as_view(), name='animals-list'),
    path('<int:pk>/', views.AnimalDetailsView.as_view(), name='animal-details'),
    path('new/', views.AnimalCreate.as_view(), name='animal-new'),
    # url('<int:question_id>/vote/', views.vote, name='vote'),
]