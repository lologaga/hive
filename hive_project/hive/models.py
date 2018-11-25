# from django.db import models
#
# # Create your models here.
# class Customer(models.Model):
#     first_name = models.CharField(max_length=264, unique=True)
#     last_name = models.CharField(max_length=264, unique = False)
#     email = models.EmailField(max_length= 1000, unique = True)
#     phone_number = models.CharField(max_length = 15)
#     address = models.CharField(max_length=4000, on_delete= models.CASCADE)
#     city = models.CharField (max_length = 264)
#     country = models.CharField (max_length = 264)
#     address_rental_station = models.CharField(Address, max_length=4000)
#
#
#     #def __repr__(self):
#         #return "<Customer {} {}>".format(self.first_name, self.last_name)
#
#     def __str__(self):
#         return self.first_name
#
#
# class VehicleType(models.Model):
#     name = models.CharField(max_length=140, unique = False)
#
#     def __str__(self):
#         return self.name
#
# class VehicleSize(models.Model):
#     name = models.CharField(max_length=140)
#
#     def __str__(self):
#         return self.name
#
# class Vehicle(models.Model):
#     vehicle = models.ForeignKey(VehicleType, on_delete= models.CASCADE, max_length=140)
#     date_created = models.DateField()
#     cost = models.FloatField()
#     size = models.ForeignKey(VehicleSize, on_delete= models.CASCADE, max_length=140)
#     station_address = models.CharField(Address,max_length= 1000)
#     def __str__(self):
#         return self.vehicule_type
#
#
# class Rental(models.Model):
#     rental_date = models.CharField(max_length=140, unique = False)
#     return_date = models.DateField()
#     customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
#     vehicle = models.ForeignKey(Vehicle, on_delete= models.CASCADE)
#
#     def __str__(self):
#         return self.rental_date
#
#
# class RentalRate(models.Model):
#     daily_rate = models.CharField(max_length=140)
#     vehicle_type = models.ForeignKey(VehicleType, on_delete= models.CASCADE)
#     vehicle_size = models.ForeignKey(VehicleSize, on_delete= models.CASCADE)
#
#     def __str__(self):
#         return self.daily_rate
#
#
# class Address(models.Model):
#     address = models.ForeignKey(max_length=4000, on_delete= models.CASCADE)
#     address2 = models.CharField(max_length=4000)
#     city = models.CharField(max_length=4000)
#     country = models.CharField(max_length=4000)
#     postal_code = models.IntergerField(max_length=4000)
#
#
# class RentalStation(models.Model):
#     name = models.CharField(max_length=4000)
#     capacity = models.IntergerField(max_length=4000)
#     address = models.ForeignKey(Address,max_length=4000, on_delete= models.CASCADE)
#
#
# class VehicleAtRentalStation(models.Model):
#     arrival_date = models.DateField()
#     departure_date = models.DateField()
#     vehicle = models.CharField(Vehicle, max_length=1000)