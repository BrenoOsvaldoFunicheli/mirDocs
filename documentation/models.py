from django.db import models


class TypeComponent(models.Model):
    type = models.CharField(max_length=100)


# Create your models here.
class PostBlog(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    link = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    type = models.ForeignKey(TypeComponent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
