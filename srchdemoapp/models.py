from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('srchdemoapp:listings_by_category', args=[self.slug])


class Listing(models.Model):
    category = models.ForeignKey(Category, related_name='listings')
    name = models.CharField(unique=True, max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
