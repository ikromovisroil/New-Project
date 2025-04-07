# Generated by Django 5.1.7 on 2025-04-05 13:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_pest'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Confidence_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_creat', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'confidence_level',
            },
        ),
        migrations.CreateModel(
            name='Opros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_creat', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'opros',
            },
        ),
        migrations.CreateModel(
            name='Summary_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_creat', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'summary_rating',
            },
        ),
        migrations.RenameField(
            model_name='pest',
            old_name='category',
            new_name='analysis',
        ),
        migrations.AddField(
            model_name='analysis',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Opros_body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('date_creat', models.DateField(auto_now_add=True)),
                ('opros', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.opros')),
            ],
            options={
                'db_table': 'opros_body',
            },
        ),
        migrations.CreateModel(
            name='Opros_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('date_creat', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('confidence_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.confidence_level')),
                ('pest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pest')),
                ('opros_body', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.opros_body')),
                ('summary_rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.summary_rating')),
            ],
            options={
                'db_table': 'opros_answer',
            },
        ),
    ]
