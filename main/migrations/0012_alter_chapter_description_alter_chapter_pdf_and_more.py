# Generated by Django 4.2.1 on 2023-06-10 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_remarks_chapter_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='pdf',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='ppt',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
