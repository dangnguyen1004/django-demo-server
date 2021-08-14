from django.shortcuts import render
from django.http import HttpResponse
from films.models import Genre, Film
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Film, Ticket, Seat, Show, Hall, User
from .serializers import (
    UserSerializer,
    FilmSerializer,
    TicketSerializer,
    HallSerializer,
    ShowSerializer,
    SeatSerializer,
)
from django.db import transaction

# Create your views here.


class FilmAPIView(APIView):
    def getFilm(self, id):
        try:
            film_query_set = (
                Film.objects.prefetch_related("actors")
                .select_related("genre")
                .get(pk=id)
            )
            film_data = FilmSerializer(film_query_set)
            return Response(data=film_data.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def getFilms(self):
        film_query_set = Film.objects.prefetch_related("actors").select_related("genre")
        film_data = FilmSerializer(film_query_set, many=True)
        return Response(data=film_data.data, status=status.HTTP_200_OK)

    def get(self, request):
        if request.query_params and "id" in request.query_params:
            id = request.query_params["id"]
            return self.getFilm(id)
        return self.getFilms()


class HallAPIView(APIView):
    def get(self, request):
        hall_query_set = Hall.objects.all()
        hall_data = HallSerializer(hall_query_set, many=True)
        return Response(data=hall_data.data, status=status.HTTP_200_OK)


class ShowAPIView(APIView):
    def getShowsOfFilm(self, film_id):
        try:
            show_query_set = Show.objects.all().filter(film=film_id).order_by('-date').order_by('-id')
            show_data = ShowSerializer(show_query_set, many=True)
            return Response(data=show_data.data, status=status.HTTP_200_OK)
        except:
            return Response(data=[],status=status.HTTP_200_OK)

    def getShows(self):
        show_query_set = Show.objects.all().order_by('-date').order_by('-id')
        show_data = ShowSerializer(show_query_set, many=True)
        return Response(data=show_data.data, status=status.HTTP_200_OK)


    def get(self, request):
        if request.query_params and 'film_id' in request.query_params:
            return self.getShowsOfFilm(request.query_params['film_id'])
        return self.getShows()

class UserAPIView(APIView):
    def getUser(self, id):
        try:
            user_query_set = User.objects.get(pk=id)
            user_data = UserSerializer(user_query_set)
            return Response(data=user_data.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        if request.query_params and "id" in request.query_params:
            id = request.query_params["id"]
            return self.getUser(id)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = request.data
        try:
            user = User()
            user.name = data["name"]
            user.gender = data["gender"]
            user.phone = data["phone"]
            user.email = data["email"]
            user.password = data["password"]
            user.save()
            return Response(data={"user_id": user.id}, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CustomerAuthAPIView(APIView):
    def post(self, request):
        data = request.data
        try:
            email = data['email']
            password = data['password']
            
            user = User.objects.get(email=email)
            if user.email == email and user.password == password:
                return Response(data={"user_id": user.id}, status=status.HTTP_200_OK)
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        except: 
            return Response(status = status.HTTP_401_UNAUTHORIZED)

class SeatAPIView(APIView):
    def get(self, request):
        if request.query_params and "ticket_id" in request.query_params:
            ticket_id = request.query_params["ticket_id"]
            seat_query_set = Seat.objects.all().filter(ticket = ticket_id)
            seat_data = SeatSerializer(seat_query_set, many=True)
            return Response(data=seat_data.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
          

class TicketAPIView(APIView):
    def getTickets(self, user_id):
        try:
            ticket_query_set = (
                Ticket.objects.select_related("show__film")
                .select_related("show__hall")
                .select_related("user")
                .filter(user=user_id)
            )
            ticket_data = TicketSerializer(ticket_query_set, many=True)
            return Response(data=ticket_data.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def getTicket(self, ticket_id):
        try:
            ticket_query_set = (
                Ticket.objects.select_related("show__film")
                .select_related("show__hall")
                .select_related("user")
                .get(pk=ticket_id)
            )
            ticket_data = TicketSerializer(ticket_query_set)
            return Response(data=ticket_data.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        if request.query_params and "user_id" in request.query_params:
            user_id = request.query_params["user_id"]
            return self.getTickets(user_id)
        if request.query_params and "ticket_id" in request.query_params:
            ticket_id = request.query_params["ticket_id"]
            return self.getTicket(ticket_id)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def createTicket(self, data):
        ticket = Ticket()
        ticket.show = Show(pk=data["show"])
        ticket.user = User(pk=data["user"])
        ticket.total_price = data["total_price"]
        ticket.save()
        return ticket.id

    def createSeat(self, ticket_id, _seat):
        seat = Seat()
        seat.ticket = Ticket(pk=ticket_id)
        seat.row = _seat["row"]
        seat.seat_number = _seat["seat_number"]
        seat.price = _seat["price"]
        seat.save()

    def post(self, request):
        data = request.data
        # return Response(data=data["show"], status=status.HTTP_200_OK)
        with transaction.atomic():
            new_ticket_id = self.createTicket(data)
            for seat in data["seats"]:
                self.createSeat(new_ticket_id, seat)

            return Response(
                data={"ticket_id": new_ticket_id}, status=status.HTTP_201_CREATED
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)
