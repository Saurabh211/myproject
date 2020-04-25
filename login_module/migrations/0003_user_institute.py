# Generated by Django 2.1.5 on 2020-04-23 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0005_remove_institute_user'),
        ('login_module', '0002_user_standard'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='institute',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='institute.Institute'),
            preserve_default=False,
        ),
    ]
