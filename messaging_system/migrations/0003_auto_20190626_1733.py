# Generated by Django 2.0.13 on 2019-06-26 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messaging_system', '0002_auto_20190618_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='users',
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='creation_date',
            field=models.DateTimeField(default='2019-06-26 17:33'),
        ),
    ]
