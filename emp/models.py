from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name=models.CharField(max_length=50)
    testimonial=models.TextField()
    picture=models.ImageField( upload_to="testimonials/")
    rating=models.PositiveIntegerField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.testimonial

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100,unique=True)
    feedback=models.TextField()