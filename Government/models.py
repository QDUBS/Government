from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


class Visitor(models.Model):
    GENDER_FEMALE = 'Female'
    GENDER_MALE = 'Male'

    GENDER_CHOICES = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male'),
    )

    STATE_CHOICES = (
        ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'),
        ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'),
        ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'),
        ('Nassarawa', 'Nassarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara'),
        ('F.C.T', 'F.C.T')
    )

    STATUS_CHOICES = (
        ('Checked In', 'Checked In'),
        ('Checked Out', 'Checked Out'),
    )

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    birth_date = models.DateField() #auto_now_add=False, auto_now=False, blank=True)
    gender = models.CharField(max_length=14, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=11) #Check out how to add country code to django phone number model field
    address = models.CharField(max_length=100)
    city_town = models.CharField(max_length=50)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    tag_no = models.IntegerField()
    purpose_of_visit = models.CharField(max_length=200)
    location_visited = models.ForeignKey(Location, on_delete=models.CASCADE)
    sign_in_time = models.TimeField(auto_now_add=True)
    sign_out_time = models.TimeField(auto_now=True)
    date_visited = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
