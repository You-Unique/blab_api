# Generated by Django 5.1.1 on 2024-10-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blabarticle', '0004_alter_article_category_alter_category_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published_category',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Business', 'Business'), ('Politics', 'Politics')], max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='topic',
            field=models.CharField(max_length=256),
        ),
    ]
