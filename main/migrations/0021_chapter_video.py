# Generated by Django 4.2.1 on 2023-06-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_chapter_pdf_alter_studentcourseenrollment_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='video',
            field=models.FileField(null=True, upload_to='store/video/'),
        ),
    ]
