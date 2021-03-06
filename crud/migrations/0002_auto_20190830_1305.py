# Generated by Django 2.2.1 on 2019-08-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='text',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='modified_at',
        ),
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Article')),
            ],
        ),
    ]
