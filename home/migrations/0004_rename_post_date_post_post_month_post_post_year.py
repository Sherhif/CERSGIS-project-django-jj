# Generated by Django 4.2 on 2024-03-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_description_2_post_description_3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_date',
            new_name='post_month',
        ),
        migrations.AddField(
            model_name='post',
            name='post_year',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
