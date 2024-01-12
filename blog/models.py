from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
