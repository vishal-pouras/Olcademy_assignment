from django.db import models

# Create your models here.

# In my model I have considered all the teams consist of 3 members


class Team(models.Model):
    teamname = models.CharField(max_length=20)          # Team Name
    member1 = models.CharField(max_length=50)           # Name of 1st member
    email1 = models.EmailField()                        # Email-id of 1st member
    contact1 = models.CharField(max_length=10)          # Contact number of 1st member
    member2 = models.CharField(max_length=50)           # Name of 2nd member
    email2 = models.EmailField()                        # Email-id of 2nd member
    contact2 = models.CharField(max_length=10)          # Contact number of 2nd member
    member3 = models.CharField(max_length=50)           # Name of 3rd member
    email3 = models.EmailField()                        # Email-id of 3rd member
    contact3 = models.CharField(max_length=10)          # Contact number of 3rd member

    def __str__(self):
        return self.teamname

