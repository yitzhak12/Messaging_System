# Generated by Django 2.0.13 on 2019-07-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging_system', '0003_auto_20190626_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creation_date',
            field=models.DateTimeField(default='2019-07-02 13:12'),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.CharField(choices=[('eitan@g.com', 'eitan@g.com'), ('kobi@g.com', 'kobi@g.com'), ('bob@g.com', 'bob@g.com')], max_length=150),
        ),
    ]
