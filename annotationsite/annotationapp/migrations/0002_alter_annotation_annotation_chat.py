# Generated by Django 4.2.6 on 2023-11-25 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotationapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='annotation',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotationapp.newusers')),
            ],
        ),
    ]