from django.db import models
from datetime import date, datetime, timedelta

# Create your models here.
class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField(blank=True, null=True)
    class Meta:
        abstract = True
        ordering = ['name']
    def get_age(self):
        age = date.today() - self.birth_date
        res = int(age.days/365)
        return res
    def __str__(self):
        return self.get_age()
class Employee(AbstractPerson):
    position = models.CharField(max_length=20)
    salary = models.IntegerField(default=0)
    work_experience = models.DateField(blank=True, null=True)

    class Meta(AbstractPerson.Meta):
        pass
    def __str__(self):
        return f' {self.name} age: {self.get_age()}'

class Passport(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    inn = models.CharField(max_length=14)
    id_card = models.CharField(max_length=20)
    def __str__(self):
        return f'Пасспорт на имя {self.name}, ИНН: {self.inn}, ID card: {self.id_card}, gender: {self.get_gender()}'
    def get_gender(self):
        if self.inn.startswith('1'):
            return f'male'
        elif self.inn.startswith('2'):
            return f'female'
class WorkProject(models.Model):
    project_name = models.CharField(max_length=20)
    members = models.ManyToManyField(Employee, related_name='work_projects', through='Membership')

class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

class Client(AbstractPerson):
    address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=14)

    class Meta(AbstractPerson.Meta):  # унаследованлось свойства Meta от PersonInfoABS и будет у нас ordering
        pass

    def __str__(self):
        return self.name

class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.PositiveSmallIntegerField()