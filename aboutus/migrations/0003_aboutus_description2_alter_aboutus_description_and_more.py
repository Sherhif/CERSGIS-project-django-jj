# Generated by Django 4.2 on 2024-03-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_alter_aboutus_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='description2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='our_mission',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='our_vision',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='why_us',
            field=models.TextField(),
        ),
    ]
