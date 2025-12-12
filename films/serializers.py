from rest_framework import serializers
from .models import Film, Director, Review, Genre
from rest_framework.exceptions import ValidationError


class DirectorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id fio birthday'.split()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


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


# class ReviewValidateSerializer(serializers.Serializer):
#     text = serializers.CharField()
#     stars = serializers.IntegerField(min_value=1, max_value=10)


class FilmValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=1, max_length=255)
    text = serializers.CharField(required=False)
    release_year = serializers.IntegerField()
    rating = serializers.FloatField(min_value=1, max_value=10)
    is_hit = serializers.BooleanField(default=True)
    director_id = serializers.IntegerField()
    genres = serializers.ListField(child=serializers.IntegerField(min_value=1))

    # reviews = serializers.ListField(child=ReviewValidateSerializer())

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError("Director does not exist!")
        return director_id

    def validate_genres(self, genres):  # [1,2,1,1,1,1,1,100]
        genres = list(set(genres))  # [1,2,100]
        genres_from_db = Genre.objects.filter(id__in=genres)  # [1,2]
        if len(genres_from_db) != len(genres):
            raise ValidationError('Genre does not exist!')
        return genres
