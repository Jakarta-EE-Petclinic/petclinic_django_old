from django.contrib import admin

from .models import Specialty
from .models import PetType
from .models import Veterinarian
from .models import Visit
from .models import Pet
from .models import Owner

admin.site.register(Specialty)
admin.site.register(PetType)
admin.site.register(Veterinarian)
admin.site.register(Visit)
admin.site.register(Pet)
admin.site.register(Owner)
