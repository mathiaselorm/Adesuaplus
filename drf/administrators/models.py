from django.db import models
import uuid
from datetime import date

class Administrators(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10,)
    profile_picture = models.ImageField(upload_to='administrator_profile_pics/', blank=True, null=True)
    administrators_id = models.CharField(max_length=20, blank=True)
    

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
    def save(self, *args, **kwargs):
        if not self.administrators_id:
            # Generate a unique student ID using UUID
            self.administrators_id = uuid.uuid4().hex[:10].upper()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name