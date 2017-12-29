from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.VisitListView.as_view(), name='visits-list'),
    url('^(?P<pk>\d+)/$', views.VisitDetailsView.as_view(), name='visit-details'),
    # url('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # url('<int:question_id>/vote/', views.vote, name='vote'),
]