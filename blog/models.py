from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model  

User = get_user_model()  

class CategoryBlog(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category_blog'
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории - Блог'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Запись')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')  
    image = models.ImageField(upload_to='cars_images', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE, verbose_name='Категория')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = 'posts'
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'Пост "{self.title}" - автор {self.author} - Добавлен {self.created_at}'

    def get_absolute_url(self):
        return reverse(f"catalog:{self.__class__.__name__.lower()}", kwargs={"post_slug": self.slug})

    def get_author_username(self):
        return self.author.username  
    
    def created_at(self):
        return self.created_at
