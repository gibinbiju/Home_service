from django.contrib import admin

# Register your models here.
from HSSapp.models import User, State, District, Area

admin.site.register(User)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Area)