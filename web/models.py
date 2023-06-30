from django.db import models

# Create your models here.

class Ciudad(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500, null=True)
    img_url = models.URLField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}'
