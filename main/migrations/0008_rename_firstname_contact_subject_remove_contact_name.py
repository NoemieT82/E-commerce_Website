# Generated by Django 4.0.6 on 2022-07-25 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_contact_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firstname',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
    ]
