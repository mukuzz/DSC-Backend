# Generated by Django 2.2.3 on 2019-09-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notices', '0011_remove_notice_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='title',
            field=models.CharField(default='title', max_length=200),
            preserve_default=False,
        ),
    ]
