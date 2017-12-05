from __future__ import unicode_literals

from django.conf.urls import url
from .views import EbiGeneSuggestListView, EbiSpeciesSuggestListView, EbiGeneListView


urlpatterns = [
    url(r'gene_suggest', EbiGeneSuggestListView.as_view()),
    url(r'gene_list', EbiGeneListView.as_view()),
    url(r'species_suggest', EbiSpeciesSuggestListView.as_view()),
]
