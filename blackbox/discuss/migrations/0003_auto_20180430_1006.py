# Generated by Django 2.0.1 on 2018-04-30 10:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0002_comment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('6d61ae0e-b31d-406e-8305-432afc4491f0'), editable=False),
        ),
    ]
