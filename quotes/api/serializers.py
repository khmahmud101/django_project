from quotes.models import Quote,QuoteCategory
from rest_framework import serializers

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('__all__')

class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCategory

        fields = ('__all__')