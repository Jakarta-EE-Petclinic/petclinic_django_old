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


class SpecialtyListView(generic.ListView):
    model = Specialty
    template_name = 'petclinic/specialty.html'
    context_object_name = 'specialty_list'


class SpecialtyFormView(generic.FormView):
    model = Specialty
    template_name = 'petclinic/specialty_form.html'
    context_object_name = 'specialty'


class PetTypeListView(generic.ListView):
    model = PetType
    template_name = 'petclinic/petType.html'
    context_object_name = 'pettype_list'


class PetTypeFormView(generic.FormView):
    model = PetType
    template_name = 'petclinic/pettype_form.html'
    context_object_name = 'pettype'


class VeterinarianListView(generic.ListView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian.html'
    context_object_name = 'veterinarian_list'


class VeterinarianFormView(generic.FormView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian_form.html'
    context_object_name = 'veterinarian'


class VisitListView(generic.ListView):
    model = Visit
    template_name = 'petclinic/visit.html'
    context_object_name = 'visit_list'


class VisitFormView(generic.FormView):
    model = Visit
    template_name = 'petclinic/visit_form.html'
    context_object_name = 'visit'


class PetListView(generic.ListView):
    model = Pet
    template_name = 'petclinic/pet.html'
    context_object_name = 'pet_list'


class PetFormView(generic.FormView):
    model = Pet
    template_name = 'petclinic/pet_form.html'
    context_object_name = 'pet'


class OwnerListView(generic.ListView):
    model = Owner
    template_name = 'petclinic/owner.html'
    context_object_name = 'owner_list'


class OwnerFormView(generic.FormView):
    model = Owner
    template_name = 'petclinic/owner_form.html'
    context_object_name = 'owner'
