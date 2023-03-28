# Generated by Django 4.1.7 on 2023-03-28 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=14)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('position', models.CharField(max_length=20)),
                ('salary', models.IntegerField(default=0)),
                ('work_experience', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advance_models.employee')),
            ],
        ),
        migrations.CreateModel(
            name='VIPClient',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='advance_models.client')),
                ('vip_status_start', models.DateField()),
                ('donation_amount', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('advance_models.client',),
        ),
        migrations.CreateModel(
            name='WorkProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
                ('members', models.ManyToManyField(related_name='work_projects', through='advance_models.Membership', to='advance_models.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=14)),
                ('id_card', models.CharField(max_length=20)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advance_models.employee')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='work_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advance_models.workproject'),
        ),
    ]