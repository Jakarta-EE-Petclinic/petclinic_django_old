from django.urls import path

from . import views

app_name = 'petclinic'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('specialty/', views.SpecialtyListView.as_view(), name='specialty'),
    path('specialty/<int:id>/', views.SpecialtyFormView.as_view(), name='specialty_form'),
    path('pettype/', views.PetTypeListView.as_view(), name='pettype'),
    path('pettype/<int:id>/', views.PetTypeFormView.as_view(), name='pettype_form'),
    path('veterinarian/', views.VeterinarianListView.as_view(), name='veterinarian'),
    path('veterinarian/<int:id>/', views.VeterinarianFormView.as_view(), name='veterinarian_form'),
    path('visit/', views.VisitListView.as_view(), name='visit'),
    path('visit/<int:id>', views.VisitFormView.as_view(), name='visit_form'),
    path('pet/', views.PetListView.as_view(), name='pet'),
    path('pet/<int:id>', views.PetFormView.as_view(), name='pet_form'),
    path('owner/', views.OwnerListView.as_view(), name='owner'),
    path('owner/<int:id>', views.OwnerFormView.as_view(), name='owner_form'),
]