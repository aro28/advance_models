from django.contrib import admin
from .models import Employee, Passport, WorkProject, Membership, Client, VIPClient
# Register your models here.
admin.site.register(Employee)
admin.site.register(Passport)
admin.site.register(WorkProject)
admin.site.register(Membership)
admin.site.register(Client)
admin.site.register(VIPClient)
