# Generated by Django 2.0 on 2018-03-21 01:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_add_event_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Event Name')),
                ('start_time', models.DateTimeField(db_index=True, help_text='Local date and time that the event starts', verbose_name='Local Start Time')),
                ('end_time', models.DateTimeField(db_index=True, help_text='Local date and time that the event ends', verbose_name='Local End Time')),
                ('summary', models.TextField(blank=True, help_text='Summary of the Event', null=True)),
                ('web_url', models.URLField(blank=True, help_text='URL for the event', null=True, verbose_name='Website')),
                ('announce_url', models.URLField(blank=True, help_text='URL for the announcement', null=True, verbose_name='Announcement')),
                ('created_time', models.DateTimeField(db_index=True, default=datetime.datetime.now, help_text='the date and time when the event was created')),
                ('tags', models.CharField(blank=True, max_length=128, null=True, verbose_name='Keyword Tags')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Category')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.City')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Country')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='owner_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_orgs', to='events.UserProfile'),
        ),
        migrations.AlterField(
            model_name='eventphoto',
            name='src',
            field=models.ImageField(upload_to='event_photos', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='team',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='events.Organization'),
        ),
        migrations.AlterField(
            model_name='team',
            name='owner_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_teams', to='events.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='avatars', verbose_name='Photo Image'),
        ),
        migrations.AddField(
            model_name='commonevent',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.UserProfile'),
        ),
        migrations.AddField(
            model_name='commonevent',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Organization'),
        ),
        migrations.AddField(
            model_name='commonevent',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_events', to='events.CommonEvent'),
        ),
        migrations.AddField(
            model_name='commonevent',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Place'),
        ),
        migrations.AddField(
            model_name='commonevent',
            name='spr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.SPR'),
        ),
        migrations.AddField(
            model_name='commonevent',
            name='topics',
            field=models.ManyToManyField(blank=True, to='events.Topic'),
        ),
        migrations.AddField(
            model_name='event',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participating_events', to='events.CommonEvent'),
        ),
    ]
