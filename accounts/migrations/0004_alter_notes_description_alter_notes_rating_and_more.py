# Generated by Django 4.2 on 2023-04-10 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notes',
            name='rating',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
