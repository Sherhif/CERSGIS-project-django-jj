from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    description_2 = models.TextField(null=True)
    description_3 = models.TextField(null=True)
    post_month = models.CharField(null=True, max_length=100)
    post_year = models.CharField(null=True, max_length=100)
    cover = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title