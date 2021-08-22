from django.db import models

# Create your models here.
class Clientes(models.Model):
    customerId = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    credit_score = models.PositiveIntegerField()
    geography = models.CharField(max_length=50)
    genders = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=genders, default='M')
    age = models.PositiveIntegerField()
    tenure = models.IntegerField()
    balance = models.FloatField()
    number_of_products = models.PositiveIntegerField()
    has_credit_card = models.BooleanField(default = False)
    active_member = models.BooleanField(default = True)
    estimated_salary = models.FloatField()
    exited = models.BooleanField(default = False)

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.customerId, self.surname)