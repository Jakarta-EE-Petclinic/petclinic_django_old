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
    template_name = 'petclinic/specialty_list.html'


class SpecialtyInputForm(forms.ModelForm):
    pass


class SpecialtyForm(generic.FormView):
    model = Specialty
    template_name = 'petclinic/specialty_form.html'
    form_class = SpecialtyInputForm


class PetTypeList(generic.ListView):
    model = PetType
    template_name = 'petclinic/pettype_list.html'


class PetTypeForm(generic.FormView):
    model = PetType
    template_name = 'petclinic/pettype_form.html'


class VeterinarianInputForm(forms.ModelForm):
    pass


class VeterinarianForm(generic.FormView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian_form.html'


class VeterinarianList(generic.ListView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian_list.html'


class VisitList(generic.ListView):
    model = Visit
    template_name = 'petclinic/visit_list.html'


class VisitForm(generic.FormView):
    model = Visit
    template_name = 'petclinic/visit_form.html'


class PetList(generic.ListView):
    model = Pet
    template_name = 'petclinic/pet_list.html'


class PetForm(generic.FormView):
    model = Pet
    template_name = 'petclinic/pet_form.html'


class OwnerList(generic.ListView):
    model = Owner
    template_name = 'petclinic/owner_list.html'


class OwnerForm(generic.FormView):
    model = Owner
    template_name = 'petclinic/owner_form.html'
