from __future__ import unicode_literals

from django.conf.urls import url
from .views import EbiGeneSuggestListView, EbiSpeciesListView, EbiOtherSpeciesListView


urlpatterns = [
    url(r'gene_suggest', EbiGeneSuggestListView.as_view()),
    url(r'gene_list', EbiOtherSpeciesListView.as_view()),
    url(r'species', EbiSpeciesListView.as_view()),
]
