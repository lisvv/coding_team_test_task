# Generated by Django 4.0.3 on 2022-03-17 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='foods.foodcategory', verbose_name='Раздел меню'),
        ),
    ]