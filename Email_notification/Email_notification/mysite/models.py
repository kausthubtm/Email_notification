from django.db import models


class Application(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    job_type = models.CharField(max_length=20)
    job_experience = models.CharField(max_length=5)
