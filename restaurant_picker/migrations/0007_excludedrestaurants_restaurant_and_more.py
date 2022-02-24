# Generated by Django 4.0.2 on 2022-02-20 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant_picker', '0006_remove_excludedrestaurants_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='excludedrestaurants',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='excluded', to='restaurant_picker.restaurant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='excludedrestaurants',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
