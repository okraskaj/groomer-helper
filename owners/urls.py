from django.urls import path

from . import views

urlpatterns = [
    path('', views.OwnerListView.as_view(), name='owners-list'),
    path('<int:pk>/', views.OwnerDetailsView.as_view(), name='owner-details'),
    path('create/', views.CreateView.as_view(), name='owner-create'),
    # url('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # url('<int:question_id>/vote/', views.vote, name='vote'),
]