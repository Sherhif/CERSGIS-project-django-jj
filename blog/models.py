from django.db import models

# Create your models here.

class BlogPage(models.Model):
    title = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100)
    title_3 = models.CharField(max_length=100)
    title_4 = models.CharField(max_length=100)
    title_5 = models.CharField(max_length=100)
    title_6 = models.CharField(max_length=100)
    description = models.TextField()
    description_2 = models.TextField()
    description_3 = models.TextField()
    description_4 = models.TextField()
    description_5 = models.TextField()
    description_6 = models.TextField()
    post_date = models.CharField(max_length=100)
    posted_by = models.CharField(null=True, max_length=100)
    cover = models.ImageField(upload_to="images/")
    cover_2 = models.ImageField(upload_to="images/")
    cover_3 = models.ImageField(upload_to="images/")
    cover_4 = models.ImageField(upload_to="images/")
    cover_5 = models.ImageField(upload_to="images/")
    cover_6 = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title