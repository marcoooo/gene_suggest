from __future__ import unicode_literals


from rest_framework import generics
from serializers import EbiGeneSuggestSerializer
from gene_suggest.models import GeneAutocomplete

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
        if query is not None:
            queryset = GeneAutocomplete.objects.filter(display_label__startswith=query)
            species = self.request.query_params.get('species', None)
            if species is not None:
                queryset.filter(species__contains=species)
            return queryset[0:self.request.query_params.get('limit', 10)]
        else:
            return GeneAutocomplete.objects.none()



