# Generated by Django 3.1.4 on 2020-12-19 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('colaboradores', '0002_auto_20201218_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
