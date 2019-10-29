from django.urls import path

from . import views

app_name = 'petclinic'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.SpecialtylView.as_view(), name='specialty'),
    path('<int:pk>/', views.PetTypelView.as_view(), name='petTypel'),
    path('<int:pk>/', views.VeterinarianView.as_view(), name='veterinarians'),
    path('<int:pk>/', views.VisitView.as_view(), name='visit'),
    path('<int:pk>/', views.PetView.as_view(), name='pet'),
    path('<int:pk>/', views.OwnerView.as_view(), name='results'),
]