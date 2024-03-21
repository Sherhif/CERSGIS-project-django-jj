from django.db import models

# Create your models here.

class BlogPage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    post_date = models.CharField(max_length=100)
    posted_by = models.CharField(null=True, max_length=100)
    cover = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title