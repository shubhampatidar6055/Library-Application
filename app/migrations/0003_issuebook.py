# Generated by Django 5.0.7 on 2024-07-19 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issuebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default=True, null=True)),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
