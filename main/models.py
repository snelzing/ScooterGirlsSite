from django.db import models


class Email(models.Model):
    email = models.EmailField()


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.ForeignKey(
        Email,
        on_delete=models.CASCADE,
    )