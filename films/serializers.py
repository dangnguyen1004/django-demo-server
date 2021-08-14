from rest_framework import serializers
from .models import Film, Genre, Actor, Hall, Show, User, Ticket, Seat

class GenreSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Genre
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)

    class Meta: 
        model = Film
        fields = '__all__'

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'
            
class ShowSerializer(serializers.ModelSerializer):
    hall = HallSerializer()
    film = FilmSerializer()

    class Meta:
        model = Show
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    show = ShowSerializer()
    user = UserSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer()

    class Meta:
        model = Seat
        fields = '__all__'