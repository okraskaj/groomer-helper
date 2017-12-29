from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BreedListView.as_view(), name='breeds-list'),
    url('^(?P<pk>\d+)/$', views.BreedDetailsView.as_view(), name='breed-details'),
    # url('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # url('<int:question_id>/vote/', views.vote, name='vote'),
]