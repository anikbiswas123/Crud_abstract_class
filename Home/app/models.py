from django.db import models


# Create your models here.
class address(models.Model):
    distr = models.CharField(max_length=400)
    sub_distr = models.CharField(max_length=300)
    address = models.TextField(max_length=400)

    class Meta:
        abstract = True


class emplopyee(address):
    emp_name=models.CharField(max_length=50)
    emp_post=models.CharField(max_length=20)
    emp_salary=models.CharField(max_length=20)

    def __str__(self):
        return self.emp_name


class customer(address):
    cust_name = models.CharField(max_length=50)
    cust_email = models.CharField(max_length=20)
    cust_Phon= models.CharField(max_length=20)

    def __str__(self):
        return self.cust_name



