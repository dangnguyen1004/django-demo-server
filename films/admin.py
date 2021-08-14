from django.contrib import admin
from . import models
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
# Register your models here.

@admin.register(models.Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'language', 'rating', 'run_time', 'release']
    list_editable = ['genre', 'run_time']
    list_per_page = 10
    list_select_related = ['genre']
    list_filter = ['genre', 'rating']
    search_fields = ['title__istartswith']
    autocomplete_fields = ['genre']

@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'avatar']
    list_per_page = 10
    search_fields = ['name__istartswith']

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'films_count']
    list_per_page = 10
    search_fields = ['title__istartswith']

    @admin.display(ordering='films_count')
    def films_count(self, genre):
        url = reverse('admin:films_film_changelist') + '?' + urlencode({
            'genre_id': str(genre.id)
        })
        return format_html('<a href="{}">{}</a>', url, genre.films_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            films_count=Count('film')
        )

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','password', 'gender', 'phone', 'email', 'tickets_count']
    list_per_page = 10
    search_fields = ['name__istartswith']
    list_filter = ['gender']

    @admin.display(ordering='tickets_count')
    def tickets_count(self, user):
        url = reverse('admin:films_ticket_changelist') + '?' + urlencode({
            'user_id': str(user.id)
        })
        return format_html('<a href="{}">{}</a>', url, user.tickets_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            tickets_count=Count('ticket')
        )


@admin.register(models.Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_seat', 'shows_count']
    list_per_page = 10
    search_fields = ['name']

    @admin.display(ordering='shows_count')
    def shows_count(self, hall):
        url = reverse('admin:films_show_changelist') + '?' + urlencode({
            'hall_id': str(hall.id)
        })
        return format_html('<a href="{}">{}</a>', url, hall.shows_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            shows_count=Count('show')
        )


@admin.register(models.Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ['hall', 'film', 'begin_time', 'end_time', 'num_of_seat']
    list_per_page = 10
    list_select_related = ['hall', 'film']
    search_fields = ['hall__istartswith', 'film__istartswith']
    autocomplete_fields = ['hall', 'film']


class SeatInline(admin.TabularInline):
    model = models.Seat
    autocomplete_fields = ['ticket']

@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['show', 'user', 'total_price', 'seats_count']
    list_per_page = 10
    search_fields = ['user__istartswith', 'show__istartswith']
    autocomplete_fields = ['show','user']
    inlines = [SeatInline]

    @admin.display(ordering='seats_count')
    def seats_count(self, ticket):
        url = reverse('admin:films_seat_changelist') + '?' + urlencode({
            'ticket_id': str(ticket.id)
        })
        return format_html('<a href="{}">{}</a>', url, ticket.seats_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            seats_count=Count('seat')
        )


@admin.register(models.Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'row', 'seat_number', 'price']
    list_per_page = 10
    list_select_related = ['ticket']
    search_fields = ['ticket__istartswith']
    autocomplete_fields = ['ticket']