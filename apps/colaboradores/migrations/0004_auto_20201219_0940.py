# Generated by Django 3.1.4 on 2020-12-19 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('colaboradores', '0003_auto_20201218_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
    ]
