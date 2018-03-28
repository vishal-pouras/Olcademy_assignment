from django.db import models

# Create your models here.


class Team(models.Model):
    teamname = models.CharField(max_length=20)
    member1 = models.CharField(max_length=50)
    email1 = models.EmailField()
    contact1 = models.CharField(max_length=10)
    member2 = models.CharField(max_length=50)
    email2 = models.EmailField()
    contact2 = models.CharField(max_length=10)
    member3 = models.CharField(max_length=50)
    email3 = models.EmailField()
    contact3 = models.CharField(max_length=10)

    def __str__(self):
        return self.teamname
