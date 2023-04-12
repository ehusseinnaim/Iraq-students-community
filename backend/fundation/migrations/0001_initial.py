# Generated by Django 4.1.7 on 2023-04-12 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customaccount', '0002_studentaccount_fundationstaffaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_funded', models.DateField()),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('staff', models.ManyToManyField(to='customaccount.fundationstaffaccount')),
                ('students', models.ManyToManyField(to='customaccount.studentaccount')),
            ],
        ),
        migrations.CreateModel(
            name='FundationStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('summary', models.TextField(max_length=1000)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customaccount.fundationstaffaccount')),
                ('fundation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fundationStages', to='fundation.fundation')),
            ],
        ),
        migrations.CreateModel(
            name='FundationStaffGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fundation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fundationStaffGroups', to='fundation.fundation')),
                ('staff', models.ManyToManyField(to='customaccount.fundationstaffaccount')),
            ],
        ),
        migrations.CreateModel(
            name='FundationEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('aotherDetails', models.TextField(max_length=500)),
                ('eventGroup', models.ManyToManyField(blank=True, to='fundation.fundationstaffgroup')),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staffLecturer', to='customaccount.fundationstaffaccount')),
                ('staffInvited', models.ManyToManyField(related_name='staffEvents', to='customaccount.fundationstaffaccount')),
                ('studentsInvited', models.ManyToManyField(related_name='studentInvites', to='customaccount.studentaccount')),
            ],
        ),
        migrations.CreateModel(
            name='FundationDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('summary', models.TextField(max_length=1000)),
                ('fundation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fundationDepartments', to='fundation.fundation')),
                ('staffAdmins', models.ManyToManyField(to='customaccount.fundationstaffaccount')),
                ('studentAdmins', models.ManyToManyField(related_name='studen', to='customaccount.studentaccount')),
                ('students', models.ManyToManyField(to='customaccount.studentaccount')),
            ],
        ),
    ]