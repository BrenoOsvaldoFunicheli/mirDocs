from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TypeComponent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    desc = models.TextField(max_length=200)
    link = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    key_term = models.CharField(max_length=100)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    key_term = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TypeOfComponent(models.Model):
    name = models.CharField(max_length=100)
    style = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(max_length=1000)
    order = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    type_ref = models.ForeignKey(TypeOfComponent, on_delete=models.CASCADE)

    def __str__(self):
        return self.type_ref.name


# order_position = models.AutoField(primary_key=False)

class KeyWord(models.Model):
    name = models.CharField(max_length=100)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
