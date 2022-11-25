from django.db import models

class News(models.Model):
    title = models.CharField("Название", max_length=100)
    image = models.ImageField(upload_to='images')
    details = models.TextField("Подробности")
    price = models.CharField("Цена", max_length=10)

    def __str__(self):
        return self.title


class Register(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=10)
