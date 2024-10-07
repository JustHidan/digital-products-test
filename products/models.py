from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('descrition'),blank=True, null=True)
    avatar = models.ImageField(blank=True, upload_to='categories')
    is_enabled = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'categories'
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(_('descrition'),blank=True, null=True)
    avatar = models.ImageField(blank=True, upload_to='categories')
    is_enabled = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category , verbose_name=_('category'))
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        db_table = 'products'
    def __str__(self):
        return self.title



class File(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='files' ,verbose_name=_('product'))
    title = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    file = models.FileField('files',upload_to='files')
    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')
        db_table = 'files'
    def __str__(self):
        return self.title

