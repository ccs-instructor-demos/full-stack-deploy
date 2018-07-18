from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    banner_image = models.ImageField(upload_to='truck_banners', blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return u'{}'.format(self.name)
