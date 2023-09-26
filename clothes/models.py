import uuid
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
        return reverse('cothes_detial', args=[str(self.id),])