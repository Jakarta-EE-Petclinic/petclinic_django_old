from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Specialty
from .models import PetType
from .models import Veterinarian
from .models import Visit
from .models import Pet
from .models import Owner


class IndexView(generic.TemplateView):
    template_name = 'petclinic/index.html'


class SpecialtylView(generic.ListView):
    model = Specialty
    template_name = 'petclinic/specialty.html'
    context_object_name = 'latest_specialty_list'

    def get_queryset(self):
        return Specialty.objects.all().order_by('-specialty_text')[:5]


class PetTypelView(generic.ListView):
    model = PetType
    template_name = 'petclinic/petType.html'
    context_object_name = 'latest_petType_list'

    def get_queryset(self):
        return PetType.objects.all().order_by('-petType_text')[:5]


class VeterinarianView(generic.ListView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian.html'
    context_object_name = 'latest_veterinarian_list'

    def get_queryset(self):
        return Veterinarian.objects.all().order_by('-veterinarian_lastName', "-veterinarian_firstName")[:5]


class VisitView(generic.ListView):
    model = Visit
    template_name = 'petclinic/visit.html'
    context_object_name = 'latest_visit_list'

    def get_queryset(self):
        return Visit.objects.all().order_by('-visit_date', "-visit_text")[:5]


class PetView(generic.ListView):
    model = Pet
    template_name = 'petclinic/pet.html'
    context_object_name = 'latest_pet_list'

    def get_queryset(self):
        return Pet.objects.all().order_by('-pet_name', "-pet_dateOfBirth")[:5]


class OwnerView(generic.ListView):
    model = Owner
    template_name = 'petclinic/owner.html'
    context_object_name = 'latest_owner_list'

    def get_queryset(self):
        return Owner.objects.all().order_by('-owner_lastName', "-owner_firstName")[:5]
