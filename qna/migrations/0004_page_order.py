# Generated by Django 4.2.4 on 2023-08-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0003_remove_page_order_remove_question_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
