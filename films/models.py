from django.db import models

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=255)

class Film(models.Model):
    actors = models.CharField(max_length=255)
    background = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    poster = models.CharField(max_length=255)
    rating = models.IntegerField()
    release = models.DateField(auto_now_add=True)
    run_time = models.IntegerField()
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

class Hall(models.Model):
    name = models.CharField(max_length=255)
    total_seat = models.IntegerField()

class Show(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    begin_time = models.TimeField()
    end_time = models.TimeField()
    num_of_seat = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    total_price = models.IntegerField()

class Seat(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    row = models.IntegerField()
    seat_number = models.IntegerField()
    price = models.IntegerField()


    
