from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import RatingStar, Rating, MoviesShort, Reviews, Actor, Genre, Movie,Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('name', 'url')
    list_display_links = ('name',)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ('title','category', 'url', 'draft', 'get_image')
    list_filter = ("category", "year")
    list_editable = ('draft',)
    readonly_fields = ('get_image',)
    search_fields = ("title", "category__name")
    save_on_top = True
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"))
        }),
        (None, {
            "fields": (("year", "world_premier", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genre", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),)


    def get_image(self,obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Постер"

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры """
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "movie","ip")

@admin.register(MoviesShort)
class MoviesShortAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"

admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ('name', 'url')


admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ('name', 'email')

admin.site.register(RatingStar)




admin.site.site_title = 'Фильмы'
admin.site.site_header = 'Фильмы'

