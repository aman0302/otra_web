from django.contrib import admin
from .models import Register, Request

# Register your models here.

class RequestModelAdmin(admin.ModelAdmin):
    list_display = ['company_name','contact_person','contact_number','budget','duration','need_design']
    class Meta:
        model =Request

class RegisterModelAdmin(admin.ModelAdmin):
    list_display = [ 'name','contact_number','car_model','commercial_or_private']
    class Meta:
        model =Register

admin.site.register(Request, RequestModelAdmin)
admin.site.register(Register, RegisterModelAdmin)

