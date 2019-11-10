from django.http import Http404
from django.shortcuts import render, get_object_or_404
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
    class Meta:
        model = Specialty
        fields = '__all__'


class SpecialtyForm(generic.FormView):
    model = Specialty
    template_name = 'petclinic/specialty_detail.html'
    form_class = SpecialtyInputForm


class SpecialtyDetail(generic.DetailView):
    model = Specialty
    template_name = 'petclinic/specialty_detail.html'

    def get_object(self):
        return get_object_or_404(Specialty, pk=self.request.user.id)


class PetTypeList(generic.ListView):
    model = PetType
    template_name = 'petclinic/pettype.html'


class PetTypeInputForm(forms.ModelForm):
    class Meta:
        model = PetType
        fields = '__all__'


class PetTypeForm(generic.FormView):
    model = PetType
    template_name = 'petclinic/pettype_detail.html'
    form_class = PetTypeInputForm


class VeterinarianList(generic.ListView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian.html'


class VeterinarianInputForm(forms.ModelForm):
    class Meta:
        model = Veterinarian
        fields = '__all__'


class VeterinarianForm(generic.FormView):
    model = Veterinarian
    template_name = 'petclinic/veterinarian_detail.html'
    form_class = VeterinarianInputForm


class VisitList(generic.ListView):
    model = Visit
    template_name = 'petclinic/visit.html'


class VisitInputForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitForm(generic.FormView):
    model = Visit
    template_name = 'petclinic/visit_detail.html'
    form_class = VisitInputForm


class PetList(generic.ListView):
    model = Pet
    template_name = 'petclinic/pet.html'


class PetInputForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class PetForm(generic.FormView):
    model = Pet
    template_name = 'petclinic/pet_detail.html'
    form_class = PetInputForm


class OwnerList(generic.ListView):
    model = Owner
    template_name = 'petclinic/owner.html'


class OwnerInputForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class OwnerForm(generic.FormView):
    model = Owner
    template_name = 'petclinic/owner_detail.html'
    form_class = OwnerInputForm
