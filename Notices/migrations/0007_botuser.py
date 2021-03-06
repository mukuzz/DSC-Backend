# Generated by Django 2.0.7 on 2019-07-16 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notices', '0006_auto_20190716_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('is_bot', models.BooleanField()),
                ('join_date_time', models.DateTimeField()),
            ],
        ),
    ]
