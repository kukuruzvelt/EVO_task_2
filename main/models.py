from django.db import models


class Usernames(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
