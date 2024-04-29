from django.db import models

class Country(models.Model):
    country_id = models.CharField(primary_key=True, max_length=10)
    country_name = models.CharField(max_length=100)
    region_id = models.IntegerField()

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = "countries"

class Location(models.Model):
    location_id = models.IntegerField()
    street_address = models.CharField(max_length=255)
    postal_code = models.IntegerField(null=True)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = "locations"
