# Generated by Django 2.0.7 on 2018-07-22 15:08

from django.db import migrations
import private_storage.fields
import private_storage.storage.files
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('small_small_hr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, help_text='A square image works best', max_length=255, upload_to='staff-images/', verbose_name='Profile Image'),
        ),
        migrations.AlterField(
            model_name='staffdocument',
            name='file',
            field=private_storage.fields.PrivateFileField(help_text='Upload staff member document', storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='staff-documents/', verbose_name='File'),
        ),
    ]
