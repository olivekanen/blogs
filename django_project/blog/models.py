from django.db import models
from django.urls import reverse 

class Posts (models.Model):
    title = models.CharField(max_length=200)
    author = author = models.ForeignKey("auth.User",on_delete=models.CASCADE,)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse("post_detail", kwargs={"pk": self.pk})