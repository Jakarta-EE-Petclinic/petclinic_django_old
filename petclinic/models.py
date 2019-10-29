from django.db import models


class Specialty(models.Model):
    specialty_text = models.CharField(max_length=200)

    def __str__(self):
        return self.specialty_text


class PetType(models.Model):
    petType_text = models.CharField(max_length=200)

    def __str__(self):
        return self.petType_text


class Veterinarian(models.Model):
    veterinarian_firstName = models.CharField(max_length=200)
    veterinarian_lastName = models.CharField(max_length=200)

    def __str__(self):
        return self.veterinarian_firstName + self.veterinarian_lastName


class Visit(models.Model):
    visit_text = models.CharField(max_length=200)
    visit_date = models.DateTimeField('date visited')

    def __str__(self):
        return self.visit_text


class Pet(models.Model):
    pet_name = models.CharField(max_length=200)
    pet_dateOfBirth = models.DateTimeField('date of birth')

    def __str__(self):
        return self.pet_name


class Owner(models.Model):
    owner_firstName = models.CharField(max_length=200)
    owner_lastName = models.CharField(max_length=200)
    owner_address = models.CharField(max_length=200)
    owner_houseNumber = models.CharField(max_length=200)
    owner_addressInfo = models.CharField(max_length=200)
    owner_city = models.CharField(max_length=200)
    owner_zipCode = models.CharField(max_length=200)
    owner_phoneNumber = models.CharField(max_length=200)

    def __str__(self):
        return self.owner_firstName + self.owner_lastName

