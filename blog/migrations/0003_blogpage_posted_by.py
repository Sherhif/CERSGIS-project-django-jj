# Generated by Django 4.2 on 2024-03-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_post_month_blogpage_post_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='posted_by',
            field=models.CharField(max_length=100, null=True),
        ),
    ]