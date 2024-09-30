import uuid  # tambahkan baris ini di paling atas
from django.db import models

from django.contrib.auth.models import User



# Create your models here.
class ShopEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # on delete = kalo delet user, 
    # semua shopentry si user ke delete
    
    # id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini

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
    
# cara bikin many ot many
# class EmployeeEntry(models.Model):
#     department = models.ManyToManyField(models.DepartmentEntry)
#     name = models.CharField(max_length=255)    
#     # id
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    
# class DepartmentEntry(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
#     name = models.CharField(max_length=255)