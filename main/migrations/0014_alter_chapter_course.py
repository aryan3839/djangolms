# Generated by Django 4.2.1 on 2023-06-13 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_chapter_pdf_remove_chapter_ppt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_chapters', to='main.course'),
        ),
    ]
