from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=120)

    def __str__(self):
        return self.name + ' - ' + self.desc
