# Generated by Django 2.1.7 on 2019-04-13 14:23

import main.mixins
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('customimage', '0002_customimage_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('og_title', models.CharField(blank=True, help_text='Fallbacks to seo title if empty', max_length=40, null=True, verbose_name='Facebook title')),
                ('og_description', models.CharField(blank=True, help_text='Fallbacks to seo description if empty', max_length=300, null=True, verbose_name='Facebook description')),
                ('twitter_title', models.CharField(blank=True, help_text='Fallbacks to facebook title if empty', max_length=40, null=True, verbose_name='Twitter title')),
                ('twitter_description', models.CharField(blank=True, help_text='Fallbacks to facebook description if empty', max_length=300, null=True, verbose_name='Twitter description')),
                ('robot_noindex', models.BooleanField(default=False, help_text='Check to add noindex to robots', verbose_name='No index')),
                ('robot_nofollow', models.BooleanField(default=False, help_text='Check to add nofollow to robots', verbose_name='No follow')),
                ('canonical_link', models.URLField(blank=True, null=True, verbose_name='Canonical link')),
            ],
            options={
                'abstract': False,
            },
            bases=(main.mixins.EnhancedEditHandlerMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.BasePage')),
                ('rich_text', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Rich text')),
            ],
            options={
                'verbose_name': 'Article',
            },
            bases=('main.basepage',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.BasePage')),
            ],
            options={
                'verbose_name': 'Home',
            },
            bases=('main.basepage',),
        ),
        migrations.AddField(
            model_name='basepage',
            name='og_image',
            field=models.ForeignKey(blank=True, help_text='If you want to override the image used on Facebook for                     this item, upload an image here.                     The recommended image size for Facebook is 1200 × 630px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='customimage.CustomImage'),
        ),
        migrations.AddField(
            model_name='basepage',
            name='twitter_image',
            field=models.ForeignKey(blank=True, help_text='Fallbacks to facebook image if empty', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='customimage.CustomImage', verbose_name='Twitter image'),
        ),
    ]
