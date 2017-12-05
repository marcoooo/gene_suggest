from __future__ import unicode_literals

from rest_framework import generics

from gene_suggest.models import GeneDataBank

from serializers import EbiGeneSuggestSerializer, EbiSpeciesSerializer, EbiOtherSpeciesSerializer


class EbiGeneSuggestListView(generics.ListAPIView):
    queryset = None
    serializer_class = EbiGeneSuggestSerializer

    def get_queryset(self):
        """
        Filtering results according to request parameters,
        no paramters, empty list
        :return:
        """
        query = self.request.query_params.get('query', None)
        if query is not None and len(query) >= 2:
            queryset = GeneDataBank.objects.filter(display_label__startswith=query)
            species = self.request.query_params.get('species', None)
            if species is not None:
                queryset.filter(species=species)
            return queryset.values('display_label').distinct()[0:self.request.query_params.get('limit', 10)]
        else:
            return GeneDataBank.objects.none()


class EbiOtherSpeciesListView(generics.ListAPIView):
    queryset = None
    serializer_class = EbiOtherSpeciesSerializer

    def get_queryset(self):
        filter_gene = self.request.query_params.get('gene', None)
        if filter_gene is not None:
            queryset = GeneDataBank.objects.filter(display_label=filter_gene)
            return queryset[0:self.request.query_params.get('limit', 100)]
        else:
            return GeneDataBank.objects.none()
        return super(EbiOtherSpeciesListView, self).get_queryset()


class EbiSpeciesListView(generics.ListAPIView):
    queryset = None
    serializer_class = EbiSpeciesSerializer

    def get_queryset(self):
        """
        Filtering results according to request parameters,
        no paramters, empty list
        :return:
        """
        return GeneDataBank.objects.all().values('species').distinct().order_by('species')
