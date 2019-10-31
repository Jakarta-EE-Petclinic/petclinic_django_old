from django.urls import path

from . import views

app_name = 'petclinic'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('specialty/', views.SpecialtyList.as_view(), name='specialty_list'),
    path('specialty/<int:id>/', views.SpecialtyForm.as_view(), name='specialty_form'),
    path('pettype/', views.PetTypeList.as_view(), name='pettype_list'),
    path('pettype/<int:id>/', views.PetTypeForm.as_view(), name='pettype_form'),
    path('veterinarian/', views.VeterinarianList.as_view(), name='veterinarian_list'),
    path('veterinarian/<int:id>/', views.VeterinarianForm.as_view(), name='veterinarian_form'),
    path('visit/', views.VisitList.as_view(), name='visit_list'),
    path('visit/<int:id>', views.VisitForm.as_view(), name='visit_form'),
    path('pet/', views.PetList.as_view(), name='pet_list'),
    path('pet/<int:id>', views.PetForm.as_view(), name='pet_form'),
    path('owner/', views.OwnerList.as_view(), name='owner_list'),
    path('owner/<int:id>', views.OwnerForm.as_view(), name='owner_form'),
]