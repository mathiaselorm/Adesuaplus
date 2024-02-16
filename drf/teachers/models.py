from django.db import models
import uuid
from datetime import date

class Teachers(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10,)
    address = models.TextField(blank=True, null=True)
    subjects_taught = models.ManyToManyField('Subject', related_name='teachers', blank=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='administrator_profile_pics/', blank=True, null=True)
    teacher_id = models.CharField(max_length=20, blank=True)
    

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
    def save(self, *args, **kwargs):
        if not self.teacher_id:
            # Generate a unique student ID using UUID
            self.teacher_id = uuid.uuid4().hex[:10].upper()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name