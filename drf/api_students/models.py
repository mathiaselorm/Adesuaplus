from django.db import models
import uuid
from datetime import date

class students(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    grade = models.CharField(max_length=10)
    student_id = models.CharField(max_length=20, blank=True)
    parent_name = models.CharField(max_length=100)
    parent_occupation = models.CharField(max_length=100)
    parent_address = models.TextField()
    guardian_phone = models.CharField(max_length=10)
    parent_email = models.EmailField()
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
    def save(self, *args, **kwargs):
        if not self.student_id:
            # Generate a unique student ID using UUID
            self.student_id = uuid.uuid4().hex[:10].upper()  
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.full_name