from django.urls import path

from . import views

app_name = 'petclinic'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('specialty/', views.SpecialtyList.as_view(), name='specialty'),
    path('specialty/<int:id>/', views.SpecialtyForm.as_view(), name='specialty'),
    path('pettype/', views.PetTypeList.as_view(), name='pettype'),
    path('pettype/<int:id>/', views.PetTypeForm.as_view(), name='pettype'),
    path('veterinarian/', views.VeterinarianList.as_view(), name='veterinarian'),
    path('veterinarian/<int:id>/', views.VeterinarianForm.as_view(), name='veterinarian'),
    path('visit/', views.VisitList.as_view(), name='visit'),
    path('visit/<int:id>', views.VisitForm.as_view(), name='visit'),
    path('pet/', views.PetList.as_view(), name='pet'),
    path('pet/<int:id>', views.PetForm.as_view(), name='pet'),
    path('owner/', views.OwnerList.as_view(), name='owner'),
    path('owner/<int:id>', views.OwnerForm.as_view(), name='owner'),
]