# Generated by Django 5.0.4 on 2024-04-23 11:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0006_thread_chatmessage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='thread',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='thread',
            name='first_person',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='second_person',
        ),
        migrations.AddField(
            model_name='platform',
            name='description',
            field=models.TextField(default='This Property is mindblowing!'),
        ),
        migrations.AddField(
            model_name='platform',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platforms.platform')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
