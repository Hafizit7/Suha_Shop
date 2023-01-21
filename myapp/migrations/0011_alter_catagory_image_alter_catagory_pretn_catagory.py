# Generated by Django 4.1.3 on 2022-12-10 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='CatagoryImages'),
        ),
        migrations.AlterField(
            model_name='catagory',
            name='pretn_catagory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='myapp.catagory'),
        ),
    ]
