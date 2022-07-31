from django.db import models
from django.contrib.auth.models import User
GENDER_CHOICES = (
    ('M','male'),
    ('F','female')
)
class PatientData(models.Model):
    patient_name = models.CharField(max_length=150,)
    mrn = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    dob = models.DateField()
    hospital_name = models.CharField(max_length=200)
    last_updated_by = models.ForeignKey(User,on_delete=models.CASCADE)
    last_updated_time = models.DateTimeField(auto_now=True)
    note_id = models.PositiveIntegerField()
    note_date_time = models.DateTimeField(auto_now_add=True)
    prescription = models.TextField(max_length=600)

    def __str__(self):
        return self.mrn