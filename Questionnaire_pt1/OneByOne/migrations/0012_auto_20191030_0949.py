# Generated by Django 2.2.6 on 2019-10-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneByOne', '0011_auto_20191013_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text_for_real_test',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='userresponsesforfeatures',
            name='choice_5',
            field=models.BooleanField(default=False, verbose_name='Feature_5'),
        ),
    ]