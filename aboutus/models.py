from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    description2 = models.TextField(null=True)
    our_mission = models.TextField()
    our_vision = models.TextField()
    why_us = models.TextField()

    def __str__(self):
        return f"{self.title}"
    # def __str__(self):
    #     return f"{self.description}"
    # def __str__(self):
    #     return f"{self.our_mission}"
    # def __str__(self):
    #     return f"{self.our_vision}"
    # def __str__(self):
    #     return f"{self.why_us}"