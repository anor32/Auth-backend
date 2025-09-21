from books.models import Book
from rest_framework import serializers
from django.utils import timezone
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['publication_date', 'owner']

    def create(self, validated_data):

        validated_data['publication_date'] = timezone.now()
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)