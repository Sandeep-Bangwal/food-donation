# Generated by Django 4.1.3 on 2023-02-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]