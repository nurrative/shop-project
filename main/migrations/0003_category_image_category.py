# Generated by Django 4.2.2 on 2023-06-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_category',
            field=models.ImageField(blank=True, null=True, upload_to='categories'),
        ),
    ]
