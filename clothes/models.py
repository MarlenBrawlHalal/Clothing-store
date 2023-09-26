import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Clothes(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=600, default=None, blank=True)
    image = models.ImageField(upload_to='images/', default=None, blank=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('clothes_detail', args=[str(self.id),])
    
class Review(models.Model):
    clothes = models.ForeignKey(
        Clothes,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    review = models.CharField(max_length=250)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.review}'