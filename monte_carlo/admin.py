from django.contrib import admin

# Register your models here.


from django.contrib import admin

from monte_carlo.models import Parameters, Assumptions
# Register your models here.
admin.site.register(Parameters)
admin.site.register(Assumptions)