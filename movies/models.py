from django.db import models
from datetime import date


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural = "Категории"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Жанры", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='actors/')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    tagline = models.TextField("Слоган", max_length=100, default=' ')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to='movies/')
    year = models.PositiveSmallIntegerField("Дата выхода", default=2020)
    country = models.CharField("Страна", max_length=100)
    directors = models.ManyToManyField("Actor", verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField('Actor', verbose_name="актеры", related_name='film_actor')
    genre = models.ManyToManyField('Genre', verbose_name='жанры')
    world_premier = models.DateField("Премьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="Сумма в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text='Сумма в долларах')
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text='Сумма в долларах')
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.SET_NULL, null=True)

    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = "Фильмы"


class RatingStar(models.Model):
    """Звезды рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"

class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField('Ip адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="ratings")
    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = "Звезды рейтинга"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = "Отзывы"

class MoviesShort(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("изображение", upload_to='movie_shots')
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = "Кадры из фильма"
