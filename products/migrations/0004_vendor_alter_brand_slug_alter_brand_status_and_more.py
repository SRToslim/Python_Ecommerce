# Generated by Django 4.2.3 on 2023-08-01 05:28

import autoslug.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_brand_slug_alter_brand_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='v_', unique=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('image', models.ImageField(default='vendor.jpg', upload_to='vendor/')),
                ('cover_image', models.ImageField(default='vendor.jpg', upload_to='vendor/')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('address', models.CharField(default='Mirpur, Dhaka', max_length=250)),
                ('contact', models.CharField(default='+8801966172000', max_length=100)),
                ('chat_resp_time', models.CharField(default='100', max_length=100)),
                ('shipping_on_time', models.CharField(default='100', max_length=100)),
                ('authentic_rating', models.CharField(default='100', max_length=100)),
                ('days_return', models.CharField(default='100', max_length=100)),
                ('warranty_period', models.CharField(default='100', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Vendors',
            },
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft'), ('disabled', 'Disabled'), ('in_review', 'In Review'), ('rejected', 'Rejected')], default='published', max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft'), ('disabled', 'Disabled'), ('in_review', 'In Review'), ('rejected', 'Rejected')], default='published', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='offer',
            field=models.CharField(blank=True, choices=[('buy1get1', 'Buy 1 Get 1'), ('Savings', 'Great Saving'), ('today_deal', "Today's Deal")], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft'), ('disabled', 'Disabled'), ('in_review', 'In Review'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('physical', 'Physical'), ('digital', 'Digital')], default='physical', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('gm', 'gm'), ('liter', 'liter'), ('dozen', 'dozen'), ('kg', 'kg'), ('box', 'box'), ('bunch', 'bunch'), ('piece', 'piece'), ('pkt', 'pkt')], max_length=100),
        ),
        migrations.AlterField(
            model_name='productvideo',
            name='provider',
            field=models.CharField(blank=True, choices=[('vimeo', 'Vimeo'), ('youtube', 'YouTube'), ('facebook', 'Facebook'), ('dailymotion', 'Dailymotion')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor', to='products.vendor'),
        ),
    ]
