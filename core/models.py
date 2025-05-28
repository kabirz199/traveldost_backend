from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.



# Destination Model

class Group(models.Model):
     name=models.CharField(max_length=150)
     url=models.URLField()
     about_us=models.TextField()
     trip_count = models.IntegerField(default=0)
     

     def __str__(self):
        return self.name
     


class Trip(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE,related_name='groups')
    trip_spot=models.CharField(max_length=100)
    trip_priority =  models.BooleanField(default=False)
    destination=models.CharField(max_length=100)
    destination_priority =  models.BooleanField(default=False)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    duration=models.CharField(max_length=50)
    url=models.URLField()

    group_priority= models.BooleanField(default=False)

    

    def __str__(self):
        return f"{self.trip_spot}---{self.group.name}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.group.trip_count += 1
            self.group.save()

    def delete(self, *args, **kwargs):
        group = self.group  # store before deleting
        super().delete(*args, **kwargs)
        group.trip_count -= 1
        group.save()


class TripImage(models.Model):
      trip=models.ForeignKey(Trip,on_delete=models.CASCADE,related_name='trip_image')
      image=CloudinaryField('image')

      def __str__(self):
        return f"Image for trip {self.trip.trip_spot}"
      
# Instagram Models

class InstagramModel(models.Model):
    username=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name