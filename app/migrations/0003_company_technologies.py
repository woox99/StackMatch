# Generated by Django 5.0.4 on 2024-04-17 05:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_remove_company_technologies"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="technologies",
            field=models.ManyToManyField(related_name="companies_using", to="app.tech"),
        ),
    ]
