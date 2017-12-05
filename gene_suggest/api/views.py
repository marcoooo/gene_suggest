from __future__ import unicode_literals

from rest_framework import generics

from gene_suggest.models import GeneDataBank

from serializers import EbiGeneSuggestSerializer, EbiSpeciesSuggestSerializer


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
            queryset = GeneDataBank.objects.filter(display_label__startswith=query).values('display_label').distinct()
            species = self.request.query_params.get('species', None)
            if species is not None:
                queryset.filter(species__contains=species)
            return queryset[0:self.request.query_params.get('limit', 10)]
        else:
            return GeneDataBank.objects.none()


class EbiGeneListView(generics.ListAPIView):
    queryset = None
    serializer_class = EbiSpeciesSuggestSerializer

    def get_queryset(self):
        filter_gene = self.request.query_params.get('gene', None)
        if filter_gene is not None:
            queryset = GeneDataBank.objects.filter(display_label=filter_gene).distinct()
            return queryset[0:self.request.query_params.get('limit', 10)]
        else:
            return GeneDataBank.objects.none()
        return super(EbiGeneListView, self).get_queryset()


class EbiSpeciesSuggestListView(generics.ListAPIView):
    queryset = None
    serializer_class = EbiSpeciesSuggestSerializer

    def get_queryset(self):
        """
        Filtering results according to request parameters,
        no paramters, empty list
        :return:
        """
        query = self.request.query_params.get('query', None)
        if query is not None and len(query) >= 2:
            queryset = GeneDataBank.objects.filter(species__startswith=query).values('species').distinct().order_by(
                'species')
            return queryset[0:self.request.query_params.get('limit', 10)]
        else:
            return GeneDataBank.objects.none()
