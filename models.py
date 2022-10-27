from django.db import models


# Create your models here.

#1. user_login - id, uname, passwd, u_type

class user_login(models.Model):
    id = models.BigAutoField(primary_key=True)
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

#6. user_details - id, user_id, fname, lname, dob, gender, addr, pin, email, contact, status

class user_details(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    dob = models.CharField(max_length=25)
    addr = models.CharField(max_length=500)
    pin = models.CharField(max_length=6)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=250)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id} {self.fname}'


#2. house_type - id, type_name
class house_type(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_name = models.CharField(max_length=100)

#3. house_manager - id, user_id, fname, lname, addr, pin, email, contact, status
class house_manager(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    addr = models.CharField(max_length=1000)
    pin = models.CharField(max_length=10)
    email = models.CharField(max_length=250)
    contact = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

#4. house_details - id, user_id, house_name, house_type_id, rent_amt, rent_advance, addr1, addr2, addr3, pin, house_decp, house_rules, house_facilities, status
class house_details(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    house_name = models.CharField(max_length=100)
    house_type_id = models.IntegerField()
    rent_amt = models.FloatField()
    rent_advance = models.CharField(max_length=100)
    addr1 = models.CharField(max_length=500)
    addr2 = models.CharField(max_length=500)
    addr3 = models.CharField(max_length=500)
    pin = models.CharField(max_length=10)
    house_descp = models.CharField(max_length=500)
    house_rules = models.CharField(max_length=500)
    house_facilities = models.CharField(max_length=500)
    house_location = models.CharField(max_length=500)
    status = models.CharField(max_length=20)

#5. house_pics - id, house_id, pic_path
class house_pics(models.Model):
    id = models.BigAutoField(primary_key=True)
    house_id = models.IntegerField()
    pic_path = models.CharField(max_length=250)


#7. house_request - id, house_id, user_id, remarks, dt, tm, status
class house_request(models.Model):
    id = models.BigAutoField(primary_key=True)
    house_id = models.IntegerField()
    user_id = models.IntegerField()
    remarks = models.CharField(max_length=1000)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

#8. user_docs - id, user_id, title, doc_file
class user_docs(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=200)
    doc_file = models.CharField(max_length=250)

#9. house_messages - id, house_request_id, user_id, user_name, message, dt, tm
class house_messages(models.Model):
    id = models.BigAutoField(primary_key=True)
    house_request_id = models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)

#10. house_agreement - id, house_id, user_id, ag_dt, rent_dt, rent_advance, rent_amt, duration, dt, tm, status
class house_agreement(models.Model):
    id = models.BigAutoField(primary_key=True)
    house_id = models.IntegerField()
    user_id = models.IntegerField()
    ag_dt = models.CharField(max_length=20)
    rent_dt = models.CharField(max_length=20)
    rent_advance = models.FloatField()
    rent_amt = models.FloatField()
    duration = models.IntegerField()
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

#11. house_pool_advertisement - id, user_id, house_id, title, descp, rent_amt, dt, tm, status
class house_pool_advertisement(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    house_id = models.IntegerField()
    title = models.CharField(max_length=50)
    descp = models.CharField(max_length=500)
    rent_amt = models.FloatField()
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

#12. house_pooling_request - id, house_pool_add_id, user_id, msg, dt, tm, status
class house_pooling_request(models.Model):
    id = models.BigAutoField(primary_key=True)
    house_pool_add_id = models.IntegerField()
    user_id = models.IntegerField()
    msg = models.CharField(max_length=500)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

#13. house_pool_details - id, house_agreement_id, user_id, dt, tm
class house_pool_details(models.Model):
    id = models.BigAutoField(primary_key=True)
    house_agreement_id = models.IntegerField()
    user_id = models.IntegerField()
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)


#14. transaction_details - id, user_id, ref_id, amt, card, cvv, dt, tm, t_type, status
class transaction_details(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    ref_id = models.IntegerField()
    amt = models.FloatField()
    card = models.CharField(max_length=20)
    cvv = models.CharField(max_length=10)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    t_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)


#15. house_rent_payment_log - id, house_agreement_id, remarks, dt, tm
class house_rent_payment_log(models.Model):
    id = models.BigAutoField(primary_key=True)
    house_agreement_id = models.IntegerField()
    remarks = models.CharField(max_length=500)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)


#16. feedback - id, house_id, user_id, rating, remarks, dt, tm, status
class feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    house_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.IntegerField()
    remarks = models.CharField(max_length=500)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
