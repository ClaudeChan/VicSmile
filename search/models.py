from django.db import models

class Clinic(models.Model):
    clinic_name = models.CharField(max_length=50)
    region = models.CharField(max_length=20)
    services = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=10)
    website = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    postcode = models.IntegerField()
    open_hour = models.CharField(max_length=200)

    def __str__(self):
        return self.clinic_name

class Dentist(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


