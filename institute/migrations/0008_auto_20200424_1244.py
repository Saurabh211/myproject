# Generated by Django 2.1.5 on 2020-04-24 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0007_subject_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=20)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'video_info',
            },
        ),
        migrations.AlterField(
            model_name='subject',
            name='institute_class',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='videos',
            name='video_sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.Subject'),
        ),
    ]
