from rest_framework import serializers
from .models import Film


class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'release_year', 'rating', 'is_hit']
        # fields = 'id title release_year rating is_hit'.split()
        # fields = '__all__'
        # exclude = 'created is_hit'.split()


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
