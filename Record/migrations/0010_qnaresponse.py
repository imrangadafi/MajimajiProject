# Generated by Django 3.2.7 on 2024-07-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record', '0009_alter_profile_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='QnAResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('response', models.TextField()),
            ],
        ),
    ]
