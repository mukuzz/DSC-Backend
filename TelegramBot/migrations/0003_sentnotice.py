# Generated by Django 2.0.7 on 2019-07-19 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notices', '0008_delete_botuser'),
        ('TelegramBot', '0002_auto_20190716_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField()),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notices.Notice')),
            ],
        ),
    ]
