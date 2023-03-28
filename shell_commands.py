from advance_models.models import *
emp1=Employee.objects.create(name="Chelovek1 Chelovekov1",birth_date="1999-03-01",position="seller", salary="10000",work_experience="2020-01-01") 
emp2=Employee.objects.create(name="Chelovek2 Chelovekov2",birth_date="1999-03-01",position="HR specialist", salary="11000",work_experience="2019-01-01")     
emp3=Employee.objects.create(name="Chelovek3 Chelovekov3",birth_date="1998-03-01",position="Security Staff", salary="8000",work_experience="2018-01-01")  
emp4=Employee.objects.create(name="Ruslan Arapov",birth_date="1991-02-28",position="Student", salary="8000",work_experience="2022-10-18") 

pass1=Passport.objects.create(name=emp1,inn="12345678",id_card="123456789")
pass2=Passport.objects.create(name=emp2,inn="22222222",id_card="223456789") 
pass3=Passport.objects.create(name=emp3,inn="13333333",id_card="123456789") 
pass4=Passport.objects.create(name=emp4,inn="24444444",id_card="123456789") 

Passport.objects.filter(name_id=1).delete()         
Employee.objects.filter(name="Chelovek1 Chelovekov1").delete() 

project1 = WorkProject.objects.create(project_name="My new projects") 
project1.members.set([emp2,emp3,emp4],through_defaults={'date_joined':'2000-01-01'}) 
project1.members.remove(emp2) 
emp5=Employee.objects.create(name="Clint Eastwood",birth_date="1930-05-31",position="Actor", salary="1000000",work_experience="1963-01-01") 

member=Membership(employee=emp5,work_project=project1,date_joined='2000-01-01')
member.save()

ilon=Client.objects.create(name='Ilon Mask',birth_date='1971-07-28',address='SpaceX Rocket Rd. Hawthorne, CA 90250',phone_number='1-800-662-7232') 
bezos=Client.objects.create(name='Jeff Bezos',birth_date='1964-01-12',address='1801 Angelo Dr Beverly Hills, CA 90210, USA',phone_number='1-888-280-4331') 
bill=Client.objects.create(name='Bill Gates',birth_date='1955-10-28',address='1835 73rd Ave NE, Medina, Washington, USA',phone_number='1-206-709-3400') 

vipclient1=VIPClient.objects.create(name="VipClient1",birth_date="1930-05-31",address="Bishkek",phone_number="001",vip_status_start="1971-07-28",donation_amount="1000000000")
vipclient2=VIPClient.objects.create(name="VipClient2",birth_date="1930-05-31",address="Bishkek",phone_number="001",vip_status_start="1964-01-12",donation_amount="2000000000")
vipclient3=VIPClient.objects.create(name="VipClient3",birth_date="1930-05-31",address="Bishkek",phone_number="001",vip_status_start="1955-10-28",donation_amount="3000000000")

Client.objects.filter(name=bill).delete()
Employee.objects.all()
Passport.objects.exclude(id_card="NULL")
WorkProject.objects.all().values()
WorkProject.objects.filter(members__name="Ruslan Arapov").values()
Client.objects.values_list()
VIPClient.objects.values_list()
