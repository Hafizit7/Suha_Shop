from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Banner (models.Model):
    titel = models.CharField(max_length=150)
    image = models.ImageField(upload_to='BannerImage')
    http_url = models.URLField(max_length=300, blank=True, null=True)

    class Meta:

        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'

    def __str__(self):
        return self.titel

class Catagory (models.Model):
    name = models.CharField(max_length = 150)
    pretn_catagory = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,  related_name='child')
    image = models.ImageField(upload_to='CatagoryImages')

    class Meta:
        verbose_name = 'Catagorys'
        verbose_name_plural = 'Catagorys'

    def __str__(self):
       return self.name

class Brand(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='BrandImages')

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
       return self.name

class Prodact(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='prodactImage')
    price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField(blank=True, null=True)
    discription = RichTextField()
    aditional_discription = RichTextField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Prodact'
        verbose_name_plural = 'Prodacts'

    def __str__(self):
        return self.name + ' / ' + str(self.id)

class Contact(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    phone = models.PositiveIntegerField(max_length = 11)
    masegge = models.fieldName = models.TextField()
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.email



class About(models.Model):
    discription = RichTextField()

    class Meta:
        
        verbose_name_plural = 'About-Us'

    def __str__(self):
        return 'About-Us'





