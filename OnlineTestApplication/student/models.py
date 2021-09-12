from django.db import models
from OnlineTestApplication import settings
# Create your models here.
User = settings.AUTH_USER_MODEL


class Student(models.Model):
    full_name = models.CharField(max_length=50,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='student/profile/', null=True, blank=True)
    address = models.CharField(max_length=50,null=True, blank=True)
    contactno = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.id)



