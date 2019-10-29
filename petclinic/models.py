from django.db import models


class Specialty(models.Model):
    specialty_text = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.specialty_text


class Veterinarian(models.Model):
    veterinarian_first_name = models.CharField(max_length=200)
    veterinarian_last_name = models.CharField(max_length=200)
    veterinarian_specialties = models.ManyToManyField(Specialty)

    def __str__(self):
        return self.veterinarian_first_name + self.veterinarian_last_name


class Owner(models.Model):
    owner_first_name = models.CharField(max_length=200)
    owner_last_name = models.CharField(max_length=200)
    owner_address = models.CharField(max_length=200)
    owner_house_number = models.CharField(max_length=200)
    owner_address_info = models.CharField(max_length=200)
    owner_city = models.CharField(max_length=200)
    owner_zip_code = models.CharField(max_length=200)
    owner_phone_number = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.owner_first_name + self.owner_last_name


class PetType(models.Model):
    pet_type_text = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.pet_type_text


class Pet(models.Model):
    pet_name = models.CharField(max_length=200)
    pet_date_of_birth = models.DateField()
    pet_type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    pet_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_name


class Visit(models.Model):
    visit_text = models.CharField(max_length=200)
    visit_date = models.DateField()
    visit_pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.visit_text

