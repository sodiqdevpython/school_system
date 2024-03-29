# Generated by Django 4.1.5 on 2023-02-15 11:09

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ustozlar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherdata',
            old_name='techerfio',
            new_name='kasbi',
        ),
        migrations.AddField(
            model_name='teacherdata',
            name='teacher_photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacherdata',
            name='teacherfio',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='teacher_info',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
