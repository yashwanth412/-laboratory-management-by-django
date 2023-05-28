from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    #confirm_password = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)

    def __str__(self):
        return self.roll_number
    
class staff(models.Model):
    staff_id = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.staff_id
    
    