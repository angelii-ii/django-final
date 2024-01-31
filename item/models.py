from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=250,verbose_name='نام')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=250,verbose_name='نام محصول')
    description=models.TextField(blank=True,null=True,verbose_name='توضیحات')
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by= models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name