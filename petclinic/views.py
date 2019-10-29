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


class IndexView(generic.ListView):
    template_name = 'petclinic/index.html'


class SpecialtylView(generic.ListView):
    model = Specialty
    template_name = 'petclinic/specialty.html'
    context_object_name = 'latest_specialty_list'

    def get_queryset(self):
        return Specialty.objects.filter(
        ).order_by('-specialty_text')[:5]


class PetTypelView(generic.ListView):
    model = PetType
    template_name = 'petclinic/petType.html'
    context_object_name = 'latest_petType_list'

    def get_queryset(self):
        return PetType.objects.filter(
        ).order_by('-petType_text')[:5]


class VeterinarianView(generic.ListView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian.html'


class VisitView(generic.ListView):
    model = Visit
    template_name = 'petclinic/visit.html'


class PetView(generic.ListView):
    model = Pet
    template_name = 'petclinic/pet.html'


class OwnerView(generic.ListView):
    model = Owner
    template_name = 'petclinic/owner.html'
