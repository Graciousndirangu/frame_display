from django.db import models

class Frame(models.Model):
    name = models.CharField(max_length=255)

class URL(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    url = models.URLField()
    duration = models.PositiveIntegerField()
    DURATION_CHOICES = [
        ('seconds', 'Seconds'),
        ('minutes', 'Minutes'),
    ]
    duration_unit = models.CharField(max_length=10, choices=DURATION_CHOICES, default= 'seconds')

