from django.db import models

class StaffMember(models.Model):
    FOCAL_CHOICES = [
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
    ]
    
    region = models.CharField(max_length=100)
    sap_id = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    primary_contact = models.CharField(max_length=20)
    secondary_contact = models.CharField(max_length=20, blank=True, null=True)
    focal_person = models.CharField(max_length=10, choices=FOCAL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.sap_id})"
