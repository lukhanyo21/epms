# Generated by Django 2.0 on 2018-03-22 00:26

import datetime
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annexture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('reference', models.CharField(blank=True, max_length=255, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Branch')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnnualTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('year_no', models.PositiveSmallIntegerField(default=0)),
                ('baseline', models.TextField(blank=True, null=True)),
                ('evidence', models.TextField(blank=True, null=True)),
                ('tf_start', models.DateField(default=datetime.date.today)),
                ('tf_end', models.DateField(default=datetime.date.today)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('goal', models.TextField(blank=True, null=True)),
                ('goal_stment', models.TextField(blank=True, null=True)),
                ('link_to_imperatives', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GoalStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('stment', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KeyPerformanceIndicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entry', models.CharField(blank=True, max_length=255, null=True)),
                ('framework', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.Framework')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LinksToPlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Branch')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('baseline', models.TextField(blank=True, null=True)),
                ('justification', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('stment', models.TextField(blank=True, null=True)),
                ('index_no', models.CharField(blank=True, max_length=5, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Branch')),
                ('framework', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.Framework')),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Programme')),
                ('sub_programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.SubProgramme')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('vision', models.TextField(blank=True, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('values', models.TextField(blank=True, null=True)),
                ('risks', models.TextField(blank=True, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Branch')),
                ('priority_p', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_programme', to='organisation.Programme')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResourcePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('overview', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('doc', models.FileField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='media/strategy/framework/rsc_plans'))),
                ('framework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.Framework')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RevisionsMandate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('heading', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('docs', models.FileField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='media/strategy/overview/rev_mandates'))),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.Overview')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('likelihood', models.CharField(blank=True, max_length=100, null=True)),
                ('impact', models.TextField(blank=True, null=True)),
                ('mit_plan', models.TextField(blank=True, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Branch')),
                ('framework', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.Framework')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SituationalAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.Overview')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StrategicOutcomeGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('goal_name', models.CharField(blank=True, max_length=100, null=True)),
                ('kra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Programme')),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.Overview')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StrategicOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('entry', models.TextField(blank=True, null=True)),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.Objective')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='keyperformanceindicator',
            name='output',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.StrategicOutput'),
        ),
        migrations.AddField(
            model_name='goalstatement',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.StrategicOutcomeGoal'),
        ),
        migrations.AddField(
            model_name='annualtarget',
            name='framework',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.Framework'),
        ),
        migrations.AddField(
            model_name='annualtarget',
            name='kpi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.KeyPerformanceIndicator'),
        ),
    ]