from django.db import models


class Profile(models.Model):

    name=models.CharField(
        max_length=120,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="enter name ...",
        help_text="enter name ...",
    )

    last_name=models.CharField(
        max_length=120,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="enter last name ...",
        help_text="enter last name ...",
    )

    phone=models.CharField(
        max_length=15,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="enter phone ...",
        help_text="enter phone ...",
    )

    email=models.EmailField(
        max_length=150,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="enter email ...",
        help_text="enter email ...",
    )