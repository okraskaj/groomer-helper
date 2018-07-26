from django.urls import path

from . import views

urlpatterns = [
    path('', views.VisitListView.as_view(), name='visits-list'),
    path('<int:pk>/', views.VisitDetailsView.as_view(), name='visit-details'),
    path('new/', views.VisitCreate.as_view(), name='visit-create'),

]