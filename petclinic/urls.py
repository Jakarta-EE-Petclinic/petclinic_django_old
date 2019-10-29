from django.urls import path

from . import views

app_name = 'petclinic'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('specialty/', views.SpecialtylView.as_view(), name='specialty'),
    path('specialty/<int:id>', views.SpecialtylView.as_view(), name='specialtyForm'),
    path('petType/', views.PetTypelView.as_view(), name='petType'),
    path('petType/<int:id>', views.PetTypelView.as_view(), name='petTypeForm'),
    path('veterinarian/', views.VeterinarianView.as_view(), name='veterinarian'),
    path('veterinarian/<int:id>/', views.VeterinarianView.as_view(), name='veterinarianForm'),
    path('visit/', views.VisitView.as_view(), name='visit'),
    path('visit/<int:id>', views.VisitView.as_view(), name='visitForm'),
    path('pet/', views.PetView.as_view(), name='pet'),
    path('pet/<int:id>', views.PetView.as_view(), name='petForm'),
    path('owner/', views.OwnerView.as_view(), name='owner'),
    path('owner/<int:id>', views.OwnerView.as_view(), name='ownerForm'),
]