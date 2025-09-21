from django.db import models
from users.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User,verbose_name='Владелец',on_delete=models.CASCADE)
    def __str__(self):
        return self.title