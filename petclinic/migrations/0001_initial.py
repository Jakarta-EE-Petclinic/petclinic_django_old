# Generated by Django 2.2.6 on 2019-10-29 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_first_name', models.CharField(max_length=200)),
                ('owner_last_name', models.CharField(max_length=200)),
                ('owner_address', models.CharField(max_length=200)),
                ('owner_house_number', models.CharField(max_length=200)),
                ('owner_address_info', models.CharField(max_length=200)),
                ('owner_city', models.CharField(max_length=200)),
                ('owner_zip_code', models.CharField(max_length=200)),
                ('owner_phone_number', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=200)),
                ('pet_date_of_birth', models.DateField()),
                ('pet_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner_pets', to='petclinic.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='PetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type_text', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty_text', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_text', models.CharField(max_length=200)),
                ('visit_date', models.DateField()),
                ('visit_pet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pet_visits', to='petclinic.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='Veterinarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veterinarian_first_name', models.CharField(max_length=200)),
                ('veterinarian_last_name', models.CharField(max_length=200)),
                ('veterinarian_specialties', models.ManyToManyField(to='petclinic.Specialty')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pet_type_pets', to='petclinic.PetType'),
        ),
    ]