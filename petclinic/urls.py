from django.urls import path

from . import views
from django.views.decorators.cache import never_cache

app_name = 'petclinic'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('specialty/', never_cache(views.SpecialtyList.as_view()), name='specialty'),
    path('specialty/<int:id>/', never_cache(views.SpecialtyDetail.as_view()), name='specialty_detail'),
    path('pettype/', never_cache(views.PetTypeList.as_view()), name='pettype'),
    path('pettype/<int:id>/', never_cache(views.PetTypeDetail.as_view()), name='pettype_detail'),
    path('veterinarian/', never_cache(views.VeterinarianList.as_view()), name='veterinarian'),
    path('veterinarian/<int:id>/', never_cache(views.VeterinarianDetail.as_view()), name='veterinarian_detail'),
    path('visit/', never_cache(views.VisitList.as_view()), name='visit'),
    path('visit/<int:id>', never_cache(views.VisitDetail.as_view()), name='visit_detail'),
    path('pet/', never_cache(views.PetList.as_view()), name='pet'),
    path('pet/<int:id>', never_cache(views.PetDetail.as_view()), name='pet_detail'),
    path('owner/', never_cache(views.OwnerList.as_view()), name='owner'),
    path('owner/<int:id>', never_cache(views.OwnerDetail.as_view()), name='owner_detail'),
]