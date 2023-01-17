# Generated by Django 4.1.5 on 2023-01-15 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='Critere',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.critere'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.PositiveIntegerField(),
        ),
    ]