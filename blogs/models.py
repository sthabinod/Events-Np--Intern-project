from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='event_static/images/blog_images')
    content = models.CharField(max_length=200)
    tags = models.CharField(max_length=100)
    featured = models.BooleanField()
    block = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)
    date_edited = models.DateField()


    