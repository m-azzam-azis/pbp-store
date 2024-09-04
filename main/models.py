from django.db import models

# Create your models here.
class ShopEntry(models.Model):
    # wajib
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    
    # optional
    sold = models.IntegerField(default=0)
    rating = models.FloatField(default=None)
    
    @property
    def is_top_seller(self):
        return self.sold > 1000 and self.rating > 4.0