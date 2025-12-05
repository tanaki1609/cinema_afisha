from rest_framework import serializers
from .models import Film, Director, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id fio'.split()


class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    genres = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Film
        fields = ['id', 'title', 'release_year', 'rating', 'is_hit', 'director', 'genres', 'reviews']
        # depth = 1

    def get_genres(self, film):
        return film.genre_list


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    text = serializers.CharField(required=False)
    release_year = serializers.IntegerField()
    rating = serializers.FloatField()
    is_hit = serializers.BooleanField(default=True)
    director_id = serializers.IntegerField()
    genres = serializers.ListField(child=serializers.IntegerField())
