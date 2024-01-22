from django.db import models

# Create your models here.

class Blog(models.Model):
    img = models.ImageField(upload_to='images/blog')
    title = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 255)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title[:50]
    
