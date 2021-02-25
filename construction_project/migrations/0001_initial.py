# Generated by Django 3.1.2 on 2020-10-26 11:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstrProjModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('users', models.ManyToManyField(related_name='constr_projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Construction_Project',
            },
        ),
    ]
