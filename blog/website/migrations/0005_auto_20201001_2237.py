# Generated by Django 3.0 on 2020-10-02 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_post_aproved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='aproved',
            new_name='approved',
        ),
    ]
