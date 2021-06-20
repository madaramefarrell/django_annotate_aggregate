from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return self.username


class Moto(models.Model):
    name = models.CharField(max_length=50)

    brand = models.ForeignKey(
        to="Accounts.Brand", related_name="moto", on_delete=models.CASCADE
    )

    buyer = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="moto")

    price = models.PositiveIntegerField(
        validators=[MinValueValidator(50000)], default=50000
    ) # price can't lower than 50k

    class Meta:
        db_table = "moto"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "brand"

    def __str__(self):
        return self.name
