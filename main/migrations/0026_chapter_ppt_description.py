# Generated by Django 4.2.1 on 2023-06-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_chapter_pdf_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='ppt_description',
            field=models.TextField(null=True),
        ),
    ]
