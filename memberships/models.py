from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200,
                                    null=True,
                                    blank=True)
    
    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name


class Membership(models.Model):
    category = models.ForeignKey('Category',
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_yearly = models.DecimalField(max_digits=6, 
                                       decimal_places=2)
    price_monthly = models.DecimalField(max_digits=6,
                                        decimal_places=2)
    price_quarterly = models.DecimalField(max_digits=6,
                                          decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
