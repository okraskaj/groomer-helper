from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AnimalListView.as_view(), name='animals-list'),
    url('^(?P<pk>\d+)/$', views.AnimalDetailsView.as_view(), name='animal-details'),
    # url('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # url('<int:question_id>/vote/', views.vote, name='vote'),
]