from django.db import models

# Create your models here.

class BeepSound(models.Model):
    name = models.CharField(max_length=100)
    path = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SayText(models.Model):
    text = models.TextField()

    def len(self):
        return len(self.text)

    def __str__(self):
        return self.text
    
    def __unicode__(self):
        return self.text
