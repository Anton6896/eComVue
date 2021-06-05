from django.db import models
from django.utils.text import slugify

from ecomCore.utils_root.product_utils import get_host, make_thumbnail


class Category(models.Model):
    """
    for one category can have multiple products
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        db_table = 'category'

    def __str__(self):
        return f"category: {self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Product(models.Model):
    """
    each product must be part of some category
    """
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', default='default.jpg')
    thumbnail = models.ImageField(upload_to='product_images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # auto generate slug field
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date_created',)
        db_table = 'product'

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"

    def get_image_url(self, request):
        if self.thumbnail:
            return f'{get_host(request)}/{self.thumbnail.url}'

        else:
            if self.image:
                # create thumbnail
                self.thumbnail = make_thumbnail(self.image)
                self.save()
                return f'{get_host(request)}/{self.thumbnail.url}'

            else:
                return ''