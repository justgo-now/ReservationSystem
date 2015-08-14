from django.db import models
from mezzanine.pages.models import Page
# Create your models here.

class Author(Page):
    dob = models.DateField("Date of birthhaha")

class Book(models.Model):
    author = models.ForeignKey("Author")
    cover = models.ImageField(upload_to="authors")


