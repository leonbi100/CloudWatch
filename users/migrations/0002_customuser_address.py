# Generated by Django 2.2.4 on 2019-08-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default='231 Gennessee St', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]