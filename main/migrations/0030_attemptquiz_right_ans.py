# Generated by Django 4.2.1 on 2023-07-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_attemptquiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='attemptquiz',
            name='right_ans',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
