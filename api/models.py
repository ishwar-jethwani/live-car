from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_save
from .utils import *
from django.contrib.auth.models import User
# authentication
# List Of cars according to city
# detail of card
# kyc of car owner


class CarOwner(models.Model):
    user                = models.OneToOneField(User,on_delete=models.CASCADE)
    fname               = models.CharField(max_length=60,verbose_name="First Name",blank=True,null=True)
    lname               = models.CharField(max_length=60,verbose_name="Last Name",blank=True,null=True)
    adharcard_no        = models.CharField(max_length=12,verbose_name="AdharCard Number",unique=True,blank=True,null=True)
    mobile_number       = PhoneNumberField(verbose_name="Mobile Number",unique=True,blank=True,null=True)
    email_id            = models.EmailField(verbose_name="Email",blank=True,null=True)
    driving_licence     = models.CharField(verbose_name="Driving Licence",max_length=16,blank=True,null=True)
    rc                  = models.CharField(max_length=10,verbose_name="Vehical Registration Number",blank=True,null=True,unique=True)
    addresss            = models.CharField(max_length=200,verbose_name="address",blank=True,null=True)
    city                = models.CharField(max_length=100,verbose_name="City Name",blank=True,null=True)
    state               = models.CharField(max_length=20,verbose_name="State Name",blank=True,null=True)
    image_of_car        = models.URLField(blank=True,null=True,verbose_name="image of car")
    img                 = models.URLField(blank=True,null=True,verbose_name="Profile Image")
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.rc

    class Meta:
        ordering = ["timestamp"]

class Movement(models.Model):
    car             = models.ForeignKey(CarOwner,on_delete=models.CASCADE)
    traveling_id    = models.CharField(max_length=20,verbose_name="Traveling ID",unique=True,blank=True)
    start_point     = models.CharField(max_length=100,verbose_name="Start Point",blank=True,null=True)
    destination     = models.CharField(max_length=100,verbose_name="Destination",blank=True,null=True)
    start_time      = models.DateTimeField(blank=True,null=True,verbose_name="Start Time")
    end_time        = models.DateTimeField(blank=True,null=True,verbose_name="End Time")
    timestamp       = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self) -> str:
        return self.car.rc+"-"+self.traveling_id+"-"+self.start_point


    








# Save Ramdom ID in Movement Instance
def pre_save_create_drive_id(sender, instance, *args, **kwargs):
    if not instance.traveling_id:
        instance.traveling_id= unique_drive_id_generator(instance)
pre_save.connect(pre_save_create_drive_id, sender=Movement)
    