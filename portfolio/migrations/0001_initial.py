# Generated by Django 3.2.13 on 2022-08-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pro_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name_plural': 'project-categories',
            },
        ),
        migrations.CreateModel(
            name='Pro_Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='./portfolio-1.jpg', upload_to='portfolio/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('project_date', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('login_require', models.BooleanField(default=False)),
                ('project_url', models.URLField(max_length=150)),
                ('category', models.ManyToManyField(to='portfolio.Pro_Category')),
                ('gallery', models.ManyToManyField(to='portfolio.Pro_Gallery')),
            ],
        ),
    ]
