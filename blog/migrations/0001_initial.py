# Generated by Django 4.2 on 2024-03-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_2', models.CharField(max_length=100)),
                ('title_3', models.CharField(max_length=100)),
                ('title_4', models.CharField(max_length=100)),
                ('title_5', models.CharField(max_length=100)),
                ('title_6', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('description_2', models.TextField()),
                ('description_3', models.TextField()),
                ('description_4', models.TextField()),
                ('description_5', models.TextField()),
                ('description_6', models.TextField()),
                ('post_month', models.CharField(max_length=100)),
                ('post_year', models.CharField(max_length=100)),
                ('post_month_2', models.CharField(max_length=100)),
                ('post_year_2', models.CharField(max_length=100)),
                ('post_month_3', models.CharField(max_length=100)),
                ('post_year_3', models.CharField(max_length=100)),
                ('post_month_4', models.CharField(max_length=100)),
                ('post_year_4', models.CharField(max_length=100)),
                ('post_month_5', models.CharField(max_length=100)),
                ('post_year_5', models.CharField(max_length=100)),
                ('post_month_6', models.CharField(max_length=100)),
                ('post_year_6', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='images/')),
                ('cover_2', models.ImageField(upload_to='images/')),
                ('cover_3', models.ImageField(upload_to='images/')),
                ('cover_4', models.ImageField(upload_to='images/')),
                ('cover_5', models.ImageField(upload_to='images/')),
                ('cover_6', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
