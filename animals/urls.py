from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnimalListView.as_view(), name='animals-list'),
    path('<int:pk>/', views.AnimalDetailsView.as_view(), name='animal-details'),
    # url('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # url('<int:question_id>/vote/', views.vote, name='vote'),
]