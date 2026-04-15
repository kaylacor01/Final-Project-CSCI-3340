from django.db import models

# Create your models here.
class FoodResource(models.Model):
  RESOURCE_TYPES = [
    ('DRIVE', 'Food Drive'),
    ('STORE', 'Economical Store'),
    ('FREE', 'Free Event'),
  ]

  name = models.CharField(max_length=200)
  address = models.TextField()
  resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
  latitude = models.FloatField()
  longitude = models.FloatField()
  description = models.TextField(blank=True)
  date_held = models.DateTimeField(null=True, blank=True) 

  def __str__(self):
    return f"{self.name}({self.get_resource_type_display()})"
