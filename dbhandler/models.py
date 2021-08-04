from django.db import models
from enums import Gender


# Create your models here.
class ContactInformation(models.Model):
    phone_number = models.IntegerField()
    email = models.EmailField()


class Person(models.Model):
    name = models.CharField(max_length=75)
    contact_information = models.OneToOneField(ContactInformation, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, choices=Gender.choices())


class Parent(Person):
    pass


class Student(Person):
    parents = models.ManyToManyField(Parent)


class Teacher(Person):
    pass


class ClassTeam(models.Model):
    team_name = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
