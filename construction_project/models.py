import os

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ConstrProjModel(models.Model):
    class Meta:
        db_table = 'Construction_Project'

    name = models.CharField(max_length=20)
    price = models.IntegerField()
    photo = models.ImageField(upload_to=os.path.join('construction_project', 'img'), default='', blank=True)

    users = models.ManyToManyField(User, related_name='constr_projects')

    def __str__(self):
        return self.name
