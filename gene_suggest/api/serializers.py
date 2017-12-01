from __future__ import unicode_literals


from rest_framework import serializers
from gene_suggest.models import GeneAutocomplete


class EbiGeneSuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneAutocomplete
        fields = ('display_label', 'species')

