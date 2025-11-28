from rest_framework import serializers
from .models import Film, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id fio'.split()


class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = ['id', 'title', 'release_year', 'rating', 'is_hit', 'director', 'genres']
        # depth = 1

    def get_genres(self, film):
        return film.genre_list


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
