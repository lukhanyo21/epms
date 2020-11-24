# Generated by Django 2.0 on 2018-03-22 00:26

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('organisation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('report_cycle', models.CharField(choices=[('Annually', 'Annually'), ('Quarterly', 'Quarterly')], max_length=15)),
                ('templates', models.FileField(null=True, upload_to=django.core.files.storage.FileSystemStorage(location='media/ppm/projects/templates'))),
                ('plan', models.FileField(null=True, upload_to=django.core.files.storage.FileSystemStorage(location='media/ppm/projects/plan'))),
                ('supporting_docs', models.FileField(null=True, upload_to='')),
                ('risk', models.TextField(null=True)),
                ('number', models.UUIDField(null=True)),
                ('details', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('comments', models.TextField(null=True)),
                ('sponsor', models.CharField(max_length=100, null=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Branch')),
                ('component', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Component')),
                ('organisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Organisation')),
                ('programme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Programme')),
                ('project_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Project Progress Status',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme_project.ProjectType'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme_project.Status'),
        ),
    ]