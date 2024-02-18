from django.db import models

# Create your models here.
class PDF(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return self.title