# Generated by Django 3.0.3 on 2020-05-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscosas', '0004_auto_20200512_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='boton',
            field=models.IntegerField(default=0),
        ),
    ]