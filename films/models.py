from django.db import models

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor)
    background = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    director = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    poster = models.CharField(max_length=255)
    rating = models.IntegerField()
    release = models.DateField(auto_now_add=True)
    run_time = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    

class NowPlaying(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Upcoming(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Hall(models.Model):
    name = models.CharField(max_length=255)
    total_seat = models.IntegerField()

    def __str__(self):
        return self.name

class Show(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    begin_time = models.TimeField()
    end_time = models.TimeField()
    num_of_seat = models.IntegerField()

    def __str__(self):
        return f'{self.film} - {self.hall} - {self.begin_time}'  

class User(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Ticket(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    total_price = models.IntegerField()

    def __str__(self):
        return f'Ticket {self.id} of show {self.show}' 

class Seat(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    row = models.CharField(max_length=255)
    seat_number = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'Seat {self.row}{self.seat_number}'


    
