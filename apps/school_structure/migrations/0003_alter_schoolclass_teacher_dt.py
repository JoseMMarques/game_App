# Generated by Django 3.2.16 on 2022-12-29 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
        ('school_structure', '0002_schoolclass_teacher_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolclass',
            name='teacher_dt',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher'),
        ),
    ]
