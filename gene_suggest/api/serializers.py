from __future__ import unicode_literals


from rest_framework import serializers
from gene_suggest.models import GeneDataBank


class EbiGeneSuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneDataBank
        fields = ('display_label',)


class EbiSpeciesSuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneDataBank
        fields = ('display_label', 'species', 'location', 'source_db', 'stable_id')
