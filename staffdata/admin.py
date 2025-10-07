from django.contrib import admin
from .models import StaffMember

@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sap_id', 'region', 'designation', 'grade', 'email', 'primary_contact', 'focal_person')
    search_fields = ('full_name', 'sap_id', 'email')
    list_filter = ('region', 'designation', 'grade', 'focal_person')