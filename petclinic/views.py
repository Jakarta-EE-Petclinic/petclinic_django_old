from django.views import generic

from .models import Specialty
from .models import PetType
from .models import Veterinarian
from .models import Visit
from .models import Pet
from .models import Owner

from django import forms


class IndexView(generic.TemplateView):
    template_name = 'petclinic/index.html'


class SpecialtyList(generic.ListView):
    model = Specialty
    template_name = 'petclinic/specialty.html'


class SpecialtyInputForm(forms.ModelForm):
    model = Specialty
    template_name = 'petclinic/specialty_form.html'


class SpecialtyForm(generic.FormView):
    model = Specialty
    template_name = 'petclinic/specialty_form.html'
    form_class = SpecialtyInputForm


class PetTypeList(generic.ListView):
    model = PetType
    template_name = 'petclinic/pettype.html'


class PetTypeForm(generic.FormView):
    model = PetType
    template_name = 'petclinic/pettype_form.html'


class VeterinarianList(generic.ListView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian.html'


class VeterinarianForm(generic.FormView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian_form.html'


class VisitList(generic.ListView):
    model = Visit
    template_name = 'petclinic/visit.html'


class VisitForm(generic.FormView):
    model = Visit
    template_name = 'petclinic/visit_form.html'


class PetList(generic.ListView):
    model = Pet
    template_name = 'petclinic/pet.html'


class PetForm(generic.FormView):
    model = Pet
    template_name = 'petclinic/pet_form.html'


class OwnerList(generic.ListView):
    model = Owner
    template_name = 'petclinic/owner.html'


class OwnerForm(generic.FormView):
    model = Owner
    template_name = 'petclinic/owner_form.html'
