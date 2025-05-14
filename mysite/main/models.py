from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, qnique=True)
    slug = models.SlugField(unique=True)


    class Meta:
        ordering = ['name',]

        indexes = [models.Index(fields=['name'])] #?

        verbose_name = 'cateory'
        verbose_name_plural = 'categries'


    def __str__(self):
        return self.name
    
    