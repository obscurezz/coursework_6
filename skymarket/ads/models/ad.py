import django_filters
from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Ad(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True, max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class AdFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ['title']
