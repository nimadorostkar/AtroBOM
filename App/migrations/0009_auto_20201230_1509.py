# Generated by Django 3.1.4 on 2020-12-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20201230_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='file',
            field=models.FileField(blank=True, default='uploads/Default.png', null=True, upload_to='uploads', verbose_name='فایل نقشه قطعه'),
        ),
    ]