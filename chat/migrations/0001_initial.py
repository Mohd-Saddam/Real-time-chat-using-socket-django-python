# Generated by Django 4.0.1 on 2023-06-14 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
                ('updated_on', models.DateTimeField(auto_now=True, db_column='updated_on')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('initiator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='convo_starter', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='convo_participant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'updated_on',
                'abstract': False,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
                ('updated_on', models.DateTimeField(auto_now=True, db_column='updated_on')),
                ('participant_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_participant_1', to=settings.AUTH_USER_MODEL)),
                ('participant_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_participant_2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'updated_on',
                'abstract': False,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
                ('updated_on', models.DateTimeField(auto_now=True, db_column='updated_on')),
                ('text', models.CharField(max_length=200)),
                ('attachment', models.FileField(blank=True, upload_to='')),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.conversation')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
    ]