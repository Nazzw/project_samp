from django.db import models

# Create your models here.
class pets(models.Model):
    In_name=models.CharField(max_length=100)
    In_des=models.CharField(max_length=100)
    In_img=models.ImageField(upload_to='In_pics')

    