# Generated by Django 5.1.1 on 2024-10-31 13:37

from django.db import migrations


def create_initial_categories(apps, schema_editor):
    title_names = ["News", 
                  "Technology", 
                  "Health & Wellness", 
                  "Sports", "Business", 
                  "Finance", 
                  "Food", 
                  "Environment",
                  "DIY & Crafts",
                  "Science",
                  "Parenting",
                  "Relationships",
                  "Career & Productivity",
                  "Spirituality",
                  "Home & Decor",
                  "Gaming",
                  ]
    
    Category = apps.get_model('blabarticle', 'Category')
    for title in title_names:
        Category.objects.create(topic=title, is_published=True)



    # Category = apps.get_model('blabarticle', 'Category')
    # Category.objects.create(title="News", is_published=True)
    # Category.objects.create(title="Technology", is_published=True)
    # Category.objects.create(title="Health & Wellness", is_published=True)
    # Category.objects.create(title="Sports", is_published=True)
    # Category.objects.create(title="Business", is_published=True)
    # Category.objects.create(title="Finance", is_published=True)
    # Category.objects.create(title="Science", is_published=True)
    # Category.objects.create(title="Food", is_published=True)
    # Category.objects.create(title="Environment", is_published=True)
    # Category.objects.create(title="DIY & Crafts", is_published=True)
    # Category.objects.create(title="Entertainment", is_published=True)
    # Category.objects.create(title="Relationships", is_published=True)
    # Category.objects.create(title="Career & Productivity", is_published=True)
    # Category.objects.create(title="Home & Decor", is_published=True)
    # Category.objects.create(title="Gaming", is_published=True)
    


class Migration(migrations.Migration):
    dependencies = [
        ('blabarticle', '0007_remove_article_published_category_and_more'),  # Replace with your app name and previous migration
    ]

    operations = [
        migrations.RunPython(create_initial_categories),
    ]