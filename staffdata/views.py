from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import StaffMember

def form_view(request):
    if request.method == 'POST':
        try:
            # Process form data
            staff_member = StaffMember(
                region=request.POST.get('region'),
                sap_id=request.POST.get('sap_id'),
                full_name=request.POST.get('full_name'),
                designation=request.POST.get('designation'),
                grade=request.POST.get('grade'),
                email=request.POST.get('email'),
                primary_contact=request.POST.get('primary_contact'),
                secondary_contact=request.POST.get('secondary_contact'),
                focal_person=request.POST.get('focal_person')
            )
            staff_member.save()
            messages.success(request, "Thank you! Your data has been recorded successfully.")
            return redirect('form')
        except IntegrityError:
            # Check if the error is due to duplicate SAP ID or email
            existing_sap = StaffMember.objects.filter(sap_id=request.POST.get('sap_id')).exists()
            existing_email = StaffMember.objects.filter(email=request.POST.get('email')).exists()
            
            if existing_sap or existing_email:
                messages.error(request, "Record already exists. You can only submit your data once.")
            else:
                messages.error(request, "An error occurred while saving your data. Please try again.")
    
    return render(request, 'staffdata/form.html')

def records_view(request):
    staff_members = StaffMember.objects.all().order_by('full_name')
    return render(request, 'staffdata/records.html', {'staff_members': staff_members})
