# Generated by Django 4.2.2 on 2023-07-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bible',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('testament', models.IntegerField(blank=True, null=True)),
                ('bookname', models.TextField(blank=True, null=True)),
                ('bookno', models.IntegerField(blank=True, null=True)),
                ('chapter', models.IntegerField(blank=True, null=True)),
                ('verseno', models.IntegerField(blank=True, null=True)),
                ('verse', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bible',
                'db_table_comment': 'jjjj\t\t',
                'managed': False,
            },
        ),
    ]
