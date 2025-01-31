# Generated by Django 5.1.1 on 2024-10-30 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blabarticle', '0003_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blabarticle.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='topic',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Business', 'Business'), ('Politics', 'Politics')], max_length=256),
        ),
    ]
