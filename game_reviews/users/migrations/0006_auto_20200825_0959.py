# Generated by Django 3.1 on 2020-08-25 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200825_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercommentsscore',
            name='created',
        ),
        migrations.RemoveField(
            model_name='usercommentsscore',
            name='updated',
        ),
    ]