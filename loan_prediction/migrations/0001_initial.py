# Generated by Django 3.2.8 on 2022-04-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PipelineInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('name_slug', models.SlugField(max_length=900)),
                ('pipeline', models.FileField(upload_to='pipeline/')),
            ],
        ),
    ]
