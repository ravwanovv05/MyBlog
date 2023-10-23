from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

