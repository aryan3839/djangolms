# Generated by Django 4.2.1 on 2023-06-10 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_chapter_description_alter_chapter_pdf_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='ppt',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='video',
        ),
    ]
