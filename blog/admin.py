from django.contrib import admin
from blog import models
from blog.models import Contact


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author', 'created_at')


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')


@admin.register(models.AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'created_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')

