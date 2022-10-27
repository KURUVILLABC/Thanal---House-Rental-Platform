from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

#################### ADMIN #########################################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['admin_name'] = ul[0].uname
            request.session['admin_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['admin_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['admin_name']
        del request.session['admin_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['admin_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)


from .models import house_type


def admin_house_type_add(request):
    if request.method == "POST":
        type_name = request.POST.get('type_name')
        house_obj = house_type(type_name = type_name)
        house_obj.save()
        context = {'msg':'New house type added'}
        return render(request, './myapp/admin_house_type_add.html',context)
    else:
        return render(request, './myapp/admin_house_type_add.html')


def admin_house_type_view(request):
    type_list = house_type.objects.all()
    context = {'type_list':type_list}
    return render(request, './myapp/admin_house_type_view.html',context)


def admin_house_type_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = house_type.objects.get(id=int(id))
    cg.delete()
    msg = 'House type removed'

    type_list = house_type.objects.all()
    context = {'type_list': type_list, 'msg':msg}
    return render(request, './myapp/admin_house_type_view.html', context)


def admin_house_type_edit(request):
    if request.method == 'POST':
        e_id = request.POST.get('e_id')
        type_name = request.POST.get('type_name')
        type_obj = house_type.objects.get(id=int(e_id))
        type_obj.type_name = type_name
        type_obj.save()

        msg = 'House type record Updated'
        type_list = house_type.objects.all()
        context = {'type_list': type_list, 'msg': msg}
        return render(request, './myapp/admin_house_type_view.html', context)
    else:
        id = request.GET.get('id')
        type_obj = house_type.objects.get(id=int(id))
        context = {'type_name': type_obj.type_name, 'e_id': type_obj.id}
        return render(request, './myapp/admin_house_type_edit.html',context)

from .models import user_details


def admin_user_details_view(request):
    user_list = user_details.objects.all()
    context = {'user_list': user_list}
    return render(request, './myapp/admin_user_details_view.html', context)

def admin_user_details_delete(request):
    try:
        uname = request.session['admin_name']
        print(uname)
    except:
        return admin_login(request)

    id = request.GET.get('id')
    print('id = '+id)
    user_obj = user_details.objects.get(id=int(id))
    user_id = user_obj.user_id
    user_obj.delete()
    user_obj = user_login.objects.get(id=int(user_id))
    user_obj.delete()

    msg = 'User Record Deleted'

    user_list = user_details.objects.all()

    context = {'user_list': user_list,  'msg':msg}
    return render(request, './myapp/admin_user_details_view.html', context)

from .models import user_docs
def admin_user_docs_view(request):
    user_id = request.GET.get('user_id')
    docs_list = user_docs.objects.filter(user_id=int(user_id))

    context = {'docs_list': docs_list, 'user_id': user_id, 'msg': ''}
    return render(request, 'myapp/admin_user_docs_view.html', context)


from .models import house_manager

def admin_owner_details_view(request):
    owner_list = house_manager.objects.filter(status='approved')
    context = {'owner_list': owner_list}
    return render(request, './myapp/admin_owner_details_view.html', context)

def admin_owner_details_delete(request):
    try:
        uname = request.session['admin_name']
        print(uname)
    except:
        return admin_login(request)

    id = request.GET.get('id')
    print('id = '+id)
    owner_obj = house_manager.objects.get(id=int(id))
    user_id = owner_obj.user_id
    owner_obj.delete()
    user_obj = user_login.objects.get(id=int(user_id))
    user_obj.delete()

    msg = 'Manager Record Deleted'

    owner_list = house_manager.objects.all()

    context = {'owner_list': owner_list,  'msg':msg}
    return render(request, './myapp/admin_owner_details_view.html', context)


def admin_owner_details_pending_view(request):
    owner_list = house_manager.objects.filter(status='pending')
    context = {'owner_list': owner_list}
    return render(request, './myapp/admin_owner_details_pending_view.html', context)


def admin_owner_details_register_update(request):
    #user_id = request.session['staff_id']
    id = request.GET.get('id')
    hm_obj = house_manager.objects.get(id=int(id))
    status = request.GET.get('status')
    if status == 'rejected':
        hm_obj.status = status
        hm_obj.save()
        context = {'msg': 'Manager rejected'}
        return render(request, 'myapp/admin_messages.html', context)
    elif status == 'approved':
        hm_obj.status = status
        hm_obj.save()
        context = {'msg': 'Manager approved'}
        return render(request, 'myapp/admin_messages.html', context)

    context = {'msg':''}
    return render(request, './myapp/admin_messages.html',context)


def admin_house_details_pending_view(request):
    #user_id = int(request.session['owner_id'])
    hd_list = house_details.objects.filter(status='pending')
    type_list = house_type.objects.all()
    hm_list = house_manager.objects.all()
    context = {'house_list': hd_list,'type_list':type_list, 'owner_list': hm_list}
    return render(request, './myapp/admin_house_details_view.html', context)

def admin_house_details_register_update(request):
    #user_id = request.session['staff_id']
    id = request.GET.get('id')
    hd_obj = house_details.objects.get(id=int(id))
    status = request.GET.get('status')
    if status == 'rejected':
        hd_obj.status = status
        hd_obj.save()
        context = {'msg': 'House rejected'}
        return render(request, 'myapp/admin_messages.html', context)
    elif status == 'approved':
        hd_obj.status = status
        hd_obj.save()
        context = {'msg': 'House approved'}
        return render(request, 'myapp/admin_messages.html', context)

    context = {'msg':''}
    return render(request, './myapp/admin_messages.html',context)


def admin_house_search(request):
    if request.method == 'POST':
        app_name = request.POST.get('app_name')
        filter = request.POST.get('filter')
        if filter == 'title':
            house_list = house_details.objects.filter(house_descp__contains=app_name)
            type_list = house_type.objects.all()
            hm_list = house_manager.objects.all()
            context = {'house_list': house_list, 'type_list': type_list, 'owner_list': hm_list}
            return render(request, './myapp/admin_house_details_view.html', context)
        elif filter == 'facilities':
            house_list = house_details.objects.filter(house_facilities__contains=app_name)
            type_list = house_type.objects.all()
            hm_list = house_manager.objects.all()
            context = {'house_list': house_list, 'type_list': type_list, 'owner_list': hm_list}
            return render(request, './myapp/admin_house_details_view.html', context)
        elif filter == 'addr':
            house_list = []
            hd_list = house_details.objects.filter(addr1__contains=app_name)
            if len(hd_list) > 0:
                house_list.extend(hd_list)
            hd_list = house_details.objects.filter(addr2__contains=app_name)
            if len(hd_list) > 0:
                house_list.extend(hd_list)
            hd_list = house_details.objects.filter(addr3__contains=app_name)
            if len(hd_list) > 0:
                house_list.extend(hd_list)

            type_list = house_type.objects.all()
            hm_list = house_manager.objects.all()
            context = {'house_list': house_list, 'type_list': type_list, 'owner_list': hm_list}
            return render(request, './myapp/admin_house_details_view.html', context)
        else:
            house_list = house_details.objects.all()
            type_list = house_type.objects.all()
            hm_list = house_manager.objects.all()
            context = {'house_list': house_list, 'type_list': type_list, 'owner_list': hm_list}
            return render(request, './myapp/admin_house_details_view.html', context)

    else:
        return render(request, 'myapp/admin_house_search.html')



############################################################################################
################################# OWNER ##################################
from .models import house_manager

def owner_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='owner')
        print(len(ul))
        if len(ul) == 1:
            hm_object = house_manager.objects.get(user_id=ul[0].id)
            if hm_object.status == 'pending':
                context = {'msg': 'Account not yet activated by Admin'}
                return render(request, 'myapp/owner_login.html', context)
            request.session['owner_id'] = ul[0].id
            request.session['owner_name'] = ul[0].uname
            context = {'uname': f'{hm_object.fname} {hm_object.lname}'}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/owner_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/owner_login.html',context)
    else:
        return render(request, 'myapp/owner_login.html')

def owner_home(request):
    try:
        user_id = int(request.session['owner_id'])
        hm_object = house_manager.objects.get(user_id=user_id)
        context = {'uname': f'{hm_object.fname} {hm_object.lname}'}
        return render(request, './myapp/owner_home.html', context)
    except:
        context = {'msg': 'Session Expired'}
        return render(request, 'myapp/owner_login.html', context)


def owner_details_add(request):
    if request.method == 'POST':
        # 3. house_manager - id, user_id, fname, lname, addr, pin, email, contact, status
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        # uname = email
        status = "pending"

        ul_obj = user_login(uname=email, passwd=password, u_type='owner')
        ul_obj.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        hm_obj = house_manager(user_id=user_id, fname=fname, lname=lname, addr=addr,
                               pin=pin, contact=contact, email=email, status=status)
        hm_obj.save()

        print(user_id)
        context = {'msg': 'House Manager Registered , Admin verification pending'}
        return render(request, 'myapp/owner_login.html',context)

    else:
        return render(request, 'myapp/owner_details_add.html')

def owner_changepassword(request):
    if request.method == 'POST':
        uname = request.session['owner_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/owner_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/owner_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/owner_changepassword.html', context)
    else:
        return render(request, './myapp/owner_changepassword.html')



def owner_logout(request):
    try:
        del request.session['owner_name']
        del request.session['owner_id']
    except:
        return owner_login_check(request)
    else:
        return owner_login_check(request)


def owner_profile_view(request):
    user_id = request.session['owner_id']
    hm_obj = house_manager.objects.get(user_id=int(user_id))
    context = {'owner_obj': hm_obj, 'e_id': hm_obj.id}
    return render(request, './myapp/owner_profile_view.html',context)

from .models import house_details

def owner_house_details_add(request):
    if request.method == 'POST':
        #4. house_details - id, user_id, house_name, house_type_id, rent_amt, rent_advance, addr1, addr2, addr3, pin, house_decp, house_rules, house_facilities, status
        user_id = int(request.session['owner_id'])
        house_name = request.POST.get('house_name')
        rent_amt = float(request.POST.get('rent_amt'))
        house_type_id = int(request.POST.get('house_type_id'))
        rent_advance = request.POST.get('rent_advance')
        addr1 = request.POST.get('addr1')
        addr2 = request.POST.get('addr2')
        addr3 = request.POST.get('addr3')
        pin = request.POST.get('pin')
        house_descp = request.POST.get('house_descp')
        house_rules = request.POST.get('house_rules')
        house_facilities = request.POST.get('house_facilities')
        house_location = request.POST.get('house_location')
        status = 'pending'


        hd_obj = house_details(
            user_id=user_id,house_name=house_name, rent_advance=rent_advance, rent_amt=rent_amt,
            house_type_id=house_type_id, addr1=addr1, addr2=addr2,addr3=addr3, pin=pin,
            house_descp=house_descp, house_rules=house_rules, house_facilities=house_facilities, status=status, house_location=house_location)

        hd_obj.save()

        print(user_id)
        context = {'msg': 'New House Registered, Admin approval pending'}
        return render(request, 'myapp/owner_messages.html',context)

    else:
        type_list = house_type.objects.all()
        context = {'type_list': type_list}
        return render(request, 'myapp/owner_house_details_add.html', context)

def owner_house_details_view(request):
    user_id = int(request.session['owner_id'])
    hd_list = house_details.objects.filter(user_id=user_id, status='approved')
    type_list = house_type.objects.all()
    context = {'house_list': hd_list,'type_list':type_list}
    return render(request, './myapp/owner_house_details_view.html', context)

def owner_house_details_pending_view(request):
    user_id = int(request.session['owner_id'])
    hd_list = house_details.objects.filter(user_id=user_id, status='pending')
    type_list = house_type.objects.all()
    context = {'house_list': hd_list,'type_list':type_list}
    return render(request, './myapp/owner_house_details_view.html', context)

def owner_house_details_rejected_view(request):
    user_id = int(request.session['owner_id'])
    hd_list = house_details.objects.filter(user_id=user_id, status='rejected')
    type_list = house_type.objects.all()
    context = {'house_list': hd_list,'type_list':type_list}
    return render(request, './myapp/owner_house_details_view.html', context)

def owner_house_details_delete(request):
    try:
        uname = request.session['owner_name']
        print(uname)
    except:
        return owner_login_check(request)

    id = request.GET.get('id')
    print('id = '+id)
    hd_obj = house_details.objects.get(id=int(id))
    hd_obj.delete()

    msg = 'House Details Deleted'

    context = {'msg':msg}
    return render(request, './myapp/owner_messages.html', context)

def owner_house_details_edit(request):
    if request.method == 'POST':
        e_id = request.POST.get('e_id')

        user_id = int(request.session['owner_id'])
        house_name = request.POST.get('house_name')
        rent_amt = float(request.POST.get('rent_amt'))
        house_type_id = int(request.POST.get('house_type_id'))
        rent_advance = request.POST.get('rent_advance')
        addr1 = request.POST.get('addr1')
        addr2 = request.POST.get('addr2')
        addr3 = request.POST.get('addr3')
        pin = request.POST.get('pin')
        house_descp = request.POST.get('house_descp')
        house_rules = request.POST.get('house_rules')
        house_facilities = request.POST.get('house_facilities')

        hd_obj = house_details.objects.get(id=int(e_id))
        hd_obj.house_name = house_name
        hd_obj.rent_amt = float(rent_amt)
        hd_obj.rent_advance = rent_advance
        hd_obj.house_type_id = house_type_id
        hd_obj.addr1 = addr1
        hd_obj.addr2 = addr2
        hd_obj.addr3 = addr3
        hd_obj.pin = pin
        hd_obj.house_descp = house_descp
        hd_obj.house_rules = house_rules
        hd_obj.house_facilities = house_facilities
        hd_obj.save()

        msg = 'House Record Updated'

        context = { 'msg': msg}
        return render(request, './myapp/owner_messages.html', context)
    else:
        id = request.GET.get('id')
        hd_obj = house_details.objects.get(id=int(id))
        type_list = house_type.objects.all()
        context = {'hd_obj': hd_obj, 'e_id': hd_obj.id, 'type_list':type_list}
        return render(request, './myapp/owner_house_details_edit.html',context)


from .models import house_pics

def owner_house_pic_add(request):
    if request.method == 'POST':
        house_id = request.POST.get('house_id')
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        pic_path = fs.save(uploaded_file.name, uploaded_file)

        hp_obj = house_pics(house_id=int(house_id),pic_path=pic_path)
        hp_obj.save()

        context = {'msg':'Picture added','house_id':house_id}
        return render(request, 'myapp/owner_house_pic_add.html',context)

    else:
        house_id = request.GET.get('house_id')
        context = {'msg':'','house_id':house_id}
        return render(request, 'myapp/owner_house_pic_add.html',context)

def owner_house_pic_delete(request):
    id = request.GET.get('id')
    house_id = request.GET.get('house_id')
    print("id="+id)
    hp_obj = house_pics.objects.get(id=int(id))
    hp_obj.delete()

    hp_list = house_pics.objects.filter(house_id=int(house_id))
    context ={'pic_list':hp_list,'house_id': house_id,'msg':'Picture deleted'}
    return render(request,'myapp/owner_house_pic_view.html',context)

def owner_house_pic_view(request):
    house_id = request.GET.get('house_id')
    hp_list = house_pics.objects.filter(house_id=int(house_id))

    context = {'pic_list': hp_list, 'house_id': house_id, 'msg': ''}
    return render(request, 'myapp/owner_house_pic_view.html', context)

def owner_house_request_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['owner_id']
    house_list = house_details.objects.filter(user_id=int(user_id))

    request_list =[]
    for house_obj in house_list:
        hr_list = house_request.objects.filter( house_id=house_obj.id, status='pending')
        if len(hr_list)>0:
            request_list.extend(hr_list)
    user_list = user_details.objects.all()
    context = {'request_list': request_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/owner_house_request_view.html', context)

def owner_house_request_view2(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['owner_id']
    house_list = house_details.objects.filter(user_id=int(user_id))

    request_list =[]
    for house_obj in house_list:
        hr_list = house_request.objects.filter( house_id=house_obj.id)
        if len(hr_list)>0:
            request_list.extend(hr_list)
    user_list = user_details.objects.all()
    context = {'request_list': request_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/owner_house_request_view2.html', context)

def owner_house_request_update(request):
    #user_id = request.session['staff_id']
    id = request.GET.get('id')
    hr_obj = house_request.objects.get(id=int(id))
    status = request.GET.get('status')
    if status == 'rejected':
        hr_obj.status = status
        hr_obj.save()
        context = {'msg': 'House request rejected'}
        return render(request, 'myapp/owner_messages.html', context)
    elif status == 'approved':
        #hr_obj.status = status
        hr_obj.save()
        context = {'msg': 'House request approved','house_request_id':id}
        return render(request, 'myapp/owner_house_agreement_add.html', context)

    context = {'msg':''}
    return render(request, './myapp/owner_messages.html',context)



def owner_user_docs_view(request):
    user_id = int(request.GET.get('user_id'))
    docs_list = user_docs.objects.filter(user_id=user_id)
    context ={'docs_list':docs_list, 'msg':''}
    return render(request,'myapp/owner_user_docs_view.html',context)


from .models import house_messages
#9. house_messages - id, house_request_id, user_id, user_name, message, dt, tm
def owner_house_messages_add(request):
    if request.method == 'POST':
        house_request_id = request.POST.get('house_request_id')
        user_id = request.session['owner_id']
        hm_obj = house_manager.objects.get(user_id=int(user_id))
        user_name = f'{hm_obj.fname} {hm_obj.lname}'
        message = request.POST.get('message')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'
        hr_obj = house_messages(house_request_id=int(house_request_id), user_id=int(user_id),
                                user_name=user_name, message=message, dt=dt, tm=tm)
        hr_obj.save()

        context = {'msg':'Message posted','house_request_id':house_request_id}
        return render(request, 'myapp/owner_messages.html',context)

    else:
        house_request_id = request.GET.get('house_request_id')
        context = {'msg':'','house_request_id':house_request_id}
        return render(request, 'myapp/owner_house_messages_add.html',context)


def owner_house_messages_view(request):
    house_request_id = request.GET.get('house_request_id')
    message_list = house_messages.objects.filter( house_request_id=int(house_request_id))
    context = {'message_list': message_list,  'msg': '', 'house_request_id':house_request_id}
    return render(request, 'myapp/owner_house_messages_view.html', context)


from .models import house_agreement
#10. house_agreement - id, house_id, user_id, ag_dt, rent_dt, rent_advance, rent_amt, duration, dt, tm, status
def owner_house_agreement_add(request):
    if request.method == 'POST':
        house_request_id = request.POST.get('house_request_id')
        hr_obj = house_request.objects.get(id=int(house_request_id))

        user_id = hr_obj.user_id
        house_id = hr_obj.house_id
        ag_dt = request.POST.get('ag_dt')
        rent_dt = request.POST.get('rent_dt')
        rent_advance = float(request.POST.get('rent_advance'))
        rent_amt = float(request.POST.get('rent_amt'))
        duration = int(request.POST.get('duration'))
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'
        ha_obj = house_agreement(house_id=house_id, user_id=user_id, ag_dt=ag_dt, rent_dt=rent_dt,
                                 rent_advance=rent_advance, rent_amt=rent_amt, duration=duration,
                                 dt=dt, tm=tm, status=status)
        ha_obj.save()
        hr_obj = house_request.objects.get(id=int(house_request_id))
        hr_obj.status='approved'
        hr_obj.save()
        context = {'msg':'Agreement posted'}
        return render(request, 'myapp/owner_messages.html',context)

    else:
        house_request_id = request.GET.get('house_request_id')
        context = {'msg':'','house_request_id':house_request_id}
        return render(request, 'myapp/owner_house_messages_add.html',context)


def owner_house_agreement_pending_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['owner_id']
    house_list = house_details.objects.filter(user_id=int(user_id))

    agreement_list =[]
    for house_obj in house_list:
        hr_list = house_agreement.objects.filter( house_id=house_obj.id, status='pending')
        if len(hr_list)>0:
            agreement_list.extend(hr_list)
    user_list = user_details.objects.all()
    context = {'agreement_list': agreement_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/owner_house_agreement_view.html', context)

def owner_house_agreement_active_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['owner_id']
    house_list = house_details.objects.filter(user_id=int(user_id))

    agreement_list =[]
    for house_obj in house_list:
        hr_list = house_agreement.objects.filter( house_id=house_obj.id, status='active')
        if len(hr_list)>0:
            agreement_list.extend(hr_list)
    user_list = user_details.objects.all()
    context = {'agreement_list': agreement_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/owner_house_agreement_view.html', context)

def owner_house_agreement_report_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['owner_id']
    house_list = house_details.objects.filter(user_id=int(user_id))

    agreement_list =[]
    for house_obj in house_list:
        hr_list = house_agreement.objects.filter( house_id=house_obj.id)
        if len(hr_list)>0:
            agreement_list.extend(hr_list)
    user_list = user_details.objects.all()
    context = {'agreement_list': agreement_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/owner_house_agreement_report_view.html', context)

def owner_transaction_details_view(request):
    ref_id = int(request.GET.get('ref_id'))
    td_list = transaction_details.objects.filter(ref_id=ref_id)
    ud_list = user_details.objects.all()
    context = {'transaction_list': td_list, 'msg': '', 'user_list': ud_list}
    return render(request, './myapp/owner_transaction_details_view.html', context)


def owner_user_details_view(request):
    user_id = request.session['owner_id']
    house_list = house_details.objects.filter(user_id=int(user_id))
    user_list = []
    for house_obj in house_list:
        ha_list = house_agreement.objects.filter(house_id=house_obj.id, status='active')
        if len(ha_list) > 0:
            for ha_obj in ha_list:
                user_obj = user_details.objects.get(user_id=ha_obj.user_id)
                user_list.append(user_obj)
    context = {'user_list': user_list}
    return render(request, './myapp/owner_user_details_view.html', context)


#################################### USER #####################################
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            user_obj = user_details.objects.get(user_id=ul[0].id)
            context = {'uname': f'{user_obj.fname} {user_obj.lname}'}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    user_id = request.session['user_id']
    user_obj = user_details.objects.get(user_id=int(user_id))
    context = {'uname': f'{user_obj.fname} {user_obj.lname}'}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", '@gmail.com')

from .models import user_docs
def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, dob=dob,addr=addr,
                          pin=pin, contact=contact, email=email, status=status )
        ud.save()
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        doc_file = fs.save(uploaded_file.name, uploaded_file)

        # 8. user_docs - id, user_id, title, doc_file
        udocs_obj = user_docs(user_id=user_id, title='Aadhaar', doc_file=doc_file)
        udocs_obj.save()
        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')


def user_details_update(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        up = user_details.objects.get(user_id=int(user_id))

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        up.fname = fname
        up.lname = lname
        up.gender = gender
        up.addr = addr
        up.pin = pin
        up.contact = contact
        up.dob = dob
        up.email = email
        up.save()


        print(user_id)
        context = {'msg': 'User Details Updated','up':up}
        return render(request, 'myapp/user_messages.html',context)

    else:
        user_id = request.session['user_id']
        up = user_details.objects.get(user_id = int(user_id))
        context={'up':up}
        return render(request, 'myapp/user_details_update.html',context)




def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


from .models import user_docs

def user_docs_add(request):
    if request.method == 'POST':
        # 8. user_docs - id, user_id, title, doc_file
        title = request.POST.get('title')
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        doc_file = fs.save(uploaded_file.name, uploaded_file)

        user_id = int(request.session['user_id'])
        udocs_obj = house_pics(user_id=int(user_id), title=title, doc_file=doc_file)
        udocs_obj.save()

        context = {'msg':'Document added',}
        return render(request, 'myapp/user_docs_add.html',context)

    else:
        #house_id = request.GET.get('house_id')
        context = {'msg':''}
        return render(request, 'myapp/user_docs_add.html',context)

def user_docs_delete(request):
    id = request.GET.get('id')

    print("id="+id)
    udocs_obj = user_docs.objects.get(id=int(id))
    udocs_obj.delete()

    user_id = int(request.session['user_id'])
    docs_list = user_docs.objects.filter(user_id=user_id)
    context ={'docs_list':docs_list, 'msg':'Document deleted'}
    return render(request,'myapp/user_docs_view.html',context)

def user_docs_view(request):
    user_id = int(request.session['user_id'])
    docs_list = user_docs.objects.filter(user_id=user_id)
    context ={'docs_list':docs_list, 'msg':''}
    return render(request,'myapp/user_docs_view.html',context)


def user_house_search(request):
    if request.method == 'POST':
        app_name = request.POST.get('app_name')
        filter = request.POST.get('filter')
        if filter == 'title':
            house_list = house_details.objects.filter(house_descp__contains=app_name)
            type_list = house_type.objects.all()
            hm_list = house_manager.objects.all()
            context = {'house_list': house_list, 'type_list': type_list, 'owner_list': hm_list}
            return render(request, './myapp/user_house_details_view.html', context)
        elif filter == 'facilities':
            house_list = house_details.objects.filter(house_facilities__contains=app_name)
            type_list = house_type.objects.all()
            hm_list = house_manager.objects.all()
            context = {'house_list': house_list, 'type_list': type_list, 'owner_list': hm_list}
            return render(request, './myapp/user_house_details_view.html', context)
        elif filter == 'addr':
            house_list = []
            hd_list = house_details.objects.filter(addr1__contains=app_name)
            if len(hd_list) > 0:
                house_list.extend(hd_list)
            hd_list = house_details.objects.filter(addr2__contains=app_name)
            if len(hd_list) > 0:
                house_list.extend(hd_list)
            hd_list = house_details.objects.filter(addr3__contains=app_name)
            if len(hd_list) > 0:
                house_list.extend(hd_list)

            type_list = house_type.objects.all()
            hm_list = house_manager.objects.all()
            context = {'house_list': house_list, 'type_list': type_list, 'owner_list': hm_list}
            return render(request, './myapp/user_house_details_view.html', context)
        else:
            house_list = house_details.objects.all()
            type_list = house_type.objects.all()
            hm_list = house_manager.objects.all()
            context = {'house_list': house_list, 'type_list': type_list, 'owner_list': hm_list}
            return render(request, './myapp/user_house_details_view.html', context)

    else:
        return render(request, 'myapp/user_house_search.html')

def user_house_pic_view(request):
    house_id = request.GET.get('house_id')
    hp_list = house_pics.objects.filter(house_id=int(house_id))

    context = {'pic_list': hp_list, 'house_id': house_id, 'msg': ''}
    return render(request, 'myapp/user_house_pic_view.html', context)

from .models import feedback
#16. feedback - id, house_id, user_id, rating, remarks, dt, tm, status
from datetime import datetime

def user_feedback_add(request):
    if request.method == 'POST':
        house_id = request.POST.get('house_id')
        user_id = request.session['user_id']
        rating = request.POST.get('rating')
        remarks = request.POST.get('remarks')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'ok'
        f_obj = feedback(house_id=int(house_id),user_id=int(user_id),rating=int(rating),remarks=remarks,
                            dt=dt,tm=tm,status=status)
        f_obj.save()

        context = {'msg':'Feedback added','house_id':house_id}
        return render(request, 'myapp/user_messages.html',context)

    else:
        house_id = request.GET.get('house_id')
        context = {'msg':'','house_id':house_id}
        return render(request, 'myapp/user_feedback_add.html',context)

def user_feedback_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    f_obj = feedback.objects.get(id=int(id))
    f_obj.delete()

    user_id = request.session['user_id']
    feedback_list = feedback.objects.filter(user_id=int(user_id))
    house_list = house_details.objects.all()
    context = {'feedback_list': feedback_list, 'house_list': house_list, 'msg': 'Feedback deleted'}
    return render(request, 'myapp/user_feedback_view.html', context)

def user_feedback_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    feedback_list = feedback.objects.filter( user_id=int(user_id))
    house_list = house_details.objects.all()
    context = {'feedback_list': feedback_list, 'house_list': house_list, 'msg': ''}
    return render(request, 'myapp/user_feedback_view.html', context)

def user_feedback_all_view(request):
    house_id = request.GET.get('house_id')
    feedback_list = feedback.objects.filter(house_id=int(house_id))
    user_list = user_details.objects.all()
    context = {'feedback_list': feedback_list, 'user_list': user_list, 'msg': ''}
    return render(request, 'myapp/user_feedback_all_view.html', context)

from .models import house_request
#7. house_request - id, house_id, user_id, remarks, dt, tm, status
def user_house_request_add(request):
    if request.method == 'POST':
        house_id = request.POST.get('house_id')
        user_id = request.session['user_id']

        remarks = request.POST.get('remarks')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'
        hr_obj = house_request(house_id=int(house_id),user_id=int(user_id),remarks=remarks,
                            dt=dt,tm=tm,status=status)
        hr_obj.save()

        context = {'msg':'House Request Added','house_id':house_id}
        return render(request, 'myapp/user_messages.html',context)

    else:
        house_id = request.GET.get('house_id')
        context = {'msg':'','house_id':house_id}
        return render(request, 'myapp/user_house_request_add.html',context)

def user_house_request_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    hr_obj = house_request.objects.get(id=int(id))
    hr_obj.delete()

    user_id = request.session['user_id']
    request_list = house_request.objects.filter(user_id=int(user_id), status='pending')
    house_list = house_details.objects.all()
    context = {'request_list': request_list, 'house_list': house_list, 'msg': 'Request deleted'}
    return render(request, 'myapp/user_feedback_view.html', context)

def user_house_request_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    request_list = house_request.objects.filter( user_id=int(user_id), status='pending')
    house_list = house_details.objects.all()
    user_list = user_details.objects.all()
    context = {'request_list': request_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/user_house_request_view.html', context)

def user_house_request_report_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    request_list = house_request.objects.filter( user_id=int(user_id))
    house_list = house_details.objects.all()
    user_list = user_details.objects.all()
    context = {'request_list': request_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/user_house_request_view.html', context)

def user_house_messages_add(request):
    if request.method == 'POST':
        house_request_id = request.POST.get('house_request_id')
        user_id = request.session['user_id']
        ud_obj = user_details.objects.get(user_id=int(user_id))
        user_name = f'{ud_obj.fname} {ud_obj.lname}'
        message = request.POST.get('message')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'
        hr_obj = house_messages(house_request_id=int(house_request_id), user_id=int(user_id),
                                user_name=user_name, message=message, dt=dt, tm=tm)
        hr_obj.save()

        context = {'msg':'Message posted','house_request_id':house_request_id}
        return render(request, 'myapp/user_messages.html',context)

    else:
        house_request_id = request.GET.get('house_request_id')
        context = {'msg':'','house_request_id':house_request_id}
        return render(request, 'myapp/user_house_messages_add.html',context)


def user_house_messages_view(request):
    house_request_id = request.GET.get('house_request_id')
    message_list = house_messages.objects.filter( house_request_id=int(house_request_id))
    context = {'message_list': message_list,  'msg': '', 'house_request_id':house_request_id}
    return render(request, 'myapp/user_house_messages_view.html', context)

def user_house_agreement_pending_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    house_list = house_details.objects.all()

    agreement_list = house_agreement.objects.filter( user_id=int(user_id), status='pending')
    user_list = user_details.objects.all()
    context = {'agreement_list': agreement_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/user_house_agreement_view.html', context)

def user_house_agreement_active_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    house_list = house_details.objects.all()

    agreement_list = house_agreement.objects.filter( user_id=int(user_id), status='active')
    user_list = user_details.objects.all()
    context = {'agreement_list': agreement_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/user_house_agreement_view.html', context)

def user_house_agreement_report_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    house_list = house_details.objects.all()

    agreement_list = house_agreement.objects.filter( user_id=int(user_id))
    user_list = user_details.objects.all()
    context = {'agreement_list': agreement_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/user_house_agreement_report_view.html', context)

from .models import transaction_details

#14. transaction_details - id, user_id, ref_id, amt, card, cvv, dt, tm, t_type, status

def user_agreement_payment_add(request):
    if request.method == 'POST':

        user_id = request.session['user_id']
        ref_id = int(request.POST.get('ref_id'))
        amt = request.POST.get('amt')
        card = request.POST.get('card')
        cvv = request.POST.get('cvv')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        t_type = 'agreement'
        status = 'paid'

        td_obj = transaction_details(amt=amt, ref_id=ref_id, user_id=int(user_id),
                                     card=card, cvv=cvv, dt=dt, tm=tm, t_type=t_type,
                                     status=status)
        td_obj.save()
        ha_obj = house_agreement.objects.get(id=ref_id)
        ha_obj.status='active'
        ha_obj.save()

        context = {'msg': 'Agreement Payed'}
        return render(request, './myapp/user_messages.html', context)
    else:
        ref_id = int(request.GET.get('ref_id'))
        ha_obj = house_agreement.objects.get(id=ref_id)
        context = { 'ref_id': ref_id, 'msg': '','amt':ha_obj.rent_advance}
        return render(request, './myapp/user_agreement_payment_add.html', context)

from .models import house_rent_payment_log
def user_rent_payment_add(request):
    if request.method == 'POST':

        user_id = request.session['user_id']
        ref_id = int(request.POST.get('ref_id'))
        amt = request.POST.get('amt')
        card = request.POST.get('card')
        cvv = request.POST.get('cvv')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        t_type = 'rent'
        status = 'paid'

        td_obj = transaction_details(amt=amt, ref_id=ref_id, user_id=int(user_id),
                                     card=card, cvv=cvv, dt=dt, tm=tm, t_type=t_type,
                                     status=status)
        td_obj.save()
        # 15. house_rent_payment_log - id, house_agreement_id, remarks, dt, tm
        remarks = f'rent paid {amt}'
        hrpl_obj = house_rent_payment_log(house_agreement_id=ref_id, dt=dt, tm=tm, remarks=remarks)
        hrpl_obj.save()
        context = {'msg': 'Rent Payed'}
        return render(request, './myapp/user_messages.html', context)
    else:
        ref_id = int(request.GET.get('ref_id'))
        ha_obj = house_agreement.objects.get(id=ref_id)
        context = { 'ref_id': ref_id, 'msg': '','amt':ha_obj.rent_amt}
        return render(request, './myapp/user_rent_payment_add.html', context)


def user_transaction_details_view(request):
    user_id = request.session['user_id']
    td_list = transaction_details.objects.filter(user_id=int(user_id))

    ud_list = user_details.objects.all()
    context = {'transaction_list': td_list, 'msg': '', 'user_list': ud_list}
    return render(request, './myapp/user_transaction_details_view.html', context)

def user_transaction_details_house_view(request):
    user_id = request.session['user_id']
    ref_id = int(request.GET.get('ref_id'))
    td_list = transaction_details.objects.filter(user_id=int(user_id),ref_id=ref_id)

    ud_list = user_details.objects.all()
    context = {'transaction_list': td_list, 'msg': '', 'user_list': ud_list}
    return render(request, './myapp/user_transaction_details_view.html', context)

from .models import house_pool_advertisement
#11. house_pool_advertisement - id, user_id, house_id, title, descp, rent_amt, dt, tm, status

def user_house_pool_advertisement_add(request):
    if request.method == 'POST':
        house_id = request.POST.get('house_id')
        user_id = request.session['user_id']
        title = request.POST.get('title')
        descp = request.POST.get('descp')
        rent_amt = request.POST.get('rent_amt')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'
        hpa_obj = house_pool_advertisement(house_id=int(house_id),user_id=int(user_id),title=title,
                                          rent_amt=rent_amt, descp=descp, dt=dt,tm=tm,status=status)
        hpa_obj.save()

        context = {'msg':'House Pool Add Added','house_id':house_id}
        return render(request, 'myapp/user_messages.html',context)

    else:
        house_id = request.GET.get('house_id')
        context = {'msg':'','house_id':house_id}
        return render(request, 'myapp/user_house_pool_advertisement_add.html',context)

def user_house_pool_advertisement_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    hr_obj = house_request.objects.get(id=int(id))
    hr_obj.delete()

    user_id = request.session['user_id']
    pool_list = house_pool_advertisement.objects.filter( user_id=int(user_id))
    user_list = user_details.objects.all()
    context = {'pool_list': pool_list,  'msg': 'Deleted', 'user_list':user_list}
    return render(request, 'myapp/user_house_pool_advertisement_view.html', context)

def user_house_pool_advertisement_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    pool_list = house_pool_advertisement.objects.filter( user_id=int(user_id))
    user_list = user_details.objects.all()
    context = {'pool_list': pool_list,  'msg': '', 'user_list':user_list}
    return render(request, 'myapp/user_house_pool_advertisement_view.html', context)

def user_house_pool_advertisement_all_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    pool_list = house_pool_advertisement.objects.all()
    house_list =[]
    for pool in pool_list:
        ha_obj = house_agreement.objects.get(id=pool.house_id)
        hhd_obj = house_details.objects.get(id=ha_obj.house_id)
        house_list.append({'id':pool.house_id, 'house_id':ha_obj.house_id,'house_name':hhd_obj.house_name})

    user_list = user_details.objects.all()
    context = {'pool_list': pool_list,  'msg': '', 'user_list':user_list, 'house_list':house_list}
    return render(request, 'myapp/user_house_pool_advertisement_all_view.html', context)


from .models import house_pooling_request
#12. house_pooling_request - id, house_pool_add_id, user_id, msg, dt, tm, status
def user_house_pooling_request_add(request):
    if request.method == 'POST':
        house_pool_add_id = request.POST.get('house_pool_add_id')
        user_id = request.session['user_id']

        msg = request.POST.get('msg')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'
        hpr_list = house_pooling_request.objects.filter(house_pool_add_id=int(house_pool_add_id),user_id=int(user_id))
        if len(hpr_list) > 0:
            context = {'msg': 'House Pooling request already added'}
            return render(request, 'myapp/user_messages.html', context)

        hpr_obj = house_pooling_request(house_pool_add_id=int(house_pool_add_id),user_id=int(user_id),msg=msg,
                            dt=dt,tm=tm,status=status)
        hpr_obj.save()

        context = {'msg':'House Pooling request added'}
        return render(request, 'myapp/user_messages.html',context)

    else:
        house_pool_add_id = request.GET.get('house_pool_add_id')
        context = {'msg':'','house_pool_add_id':house_pool_add_id}
        return render(request, 'myapp/user_house_pooling_request_add.html',context)

def user_house_pooling_request_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    hr_obj = house_pooling_request.objects.get(id=int(id))
    hr_obj.delete()

    context = { 'msg': 'Request deleted'}
    return render(request, 'myapp/user_messages.html', context)

def user_house_pooling_request_update(request):
    id = request.GET.get('id')
    status = request.GET.get('status')
    print("id="+id)
    hr_obj = house_pooling_request.objects.get(id=int(id))
    hr_obj.status = status
    hr_obj.save()

    context = { 'msg': f'Request {status}'}
    return render(request, 'myapp/user_messages.html', context)


def user_house_pooling_request_view(request):
    house_pool_add_id = request.GET.get('house_pool_add_id')
    user_id = request.session['user_id']
    request_list = house_pooling_request.objects.filter(house_pool_add_id=int(house_pool_add_id))
    house_list = []
    for r in request_list:
        hpa_obj = house_pool_advertisement.objects.get(id=r.house_pool_add_id)
        ha_obj = house_agreement.objects.get(id=hpa_obj.house_id)
        hd_obj = house_details.objects.get(id=ha_obj.house_id)
        house_list.append({'id': r.id, 'house_name': hd_obj.house_name})
    user_list = user_details.objects.all()
    context = {'request_list': request_list, 'house_list': house_list, 'msg': '', 'user_list': user_list}
    return render(request, 'myapp/user_house_pooling_request_view.html', context)


def user_house_pooling_request_pending_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    request_list = house_pooling_request.objects.filter( user_id=int(user_id), status='pending')
    house_list = []
    for r in request_list:
        hpa_obj = house_pool_advertisement.objects.get(id=r.house_pool_add_id)
        ha_obj = house_agreement.objects.get(id=hpa_obj.house_id)
        hd_obj = house_details.objects.get(id=ha_obj.house_id)
        house_list.append({'id':r.id,'house_name':hd_obj.house_name})
    user_list = user_details.objects.all()
    context = {'request_list': request_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/user_house_pooling_request_pending_view.html', context)

def user_house_pooling_request_report_view(request):
    #house_id = request.GET.get('house_id')
    user_id = request.session['user_id']
    request_list = house_pooling_request.objects.filter( user_id=int(user_id))
    house_list = []
    for r in request_list:
        hpa_obj = house_pool_advertisement.objects.get(id=r.house_pool_add_id)
        ha_obj = house_agreement.objects.get(id=hpa_obj.house_id)
        hd_obj = house_details.objects.get(id=ha_obj.house_id)
        house_list.append({'id':r.id,'house_name':hd_obj.house_name})
    user_list = user_details.objects.all()
    context = {'request_list': request_list, 'house_list': house_list, 'msg': '', 'user_list':user_list}
    return render(request, 'myapp/user_house_pooling_request_report_view.html', context)


def user_notifications_view(request):
    user_id = request.session['user_id']

    rent_list = house_agreement.objects.filter(user_id=user_id, status='active')
    dt = datetime.today().strftime('%Y-%m-%d')
    dt_details2 = dt.split('-')
    y2 = int(dt_details2[0])
    m2 = int(dt_details2[1])
    d2 = int(dt_details2[2])
    msg_list = []
    for rent_obj in rent_list:
        d1 = int(rent_obj.rent_dt)
        days = d1 - d2
        if days >=-3 and days < 0:
            msg_list.append({'title': 'House Rent',
                             'descp': f'{rent_obj.rent_amt}  on {rent_obj.rent_dt}'})
        elif days > 0:
            msg_list.append({'title': 'House Rent Due',
                             'descp': f'{rent_obj.rent_amt}  on {rent_obj.rent_dt}'})
    msg = ''
    if len(msg_list) == 0:
        context = {'msg': 'No notifications !!!!!'}
    else:
        context = {'msg':msg, 'msg_list': msg_list}
    return render(request, './myapp/user_notifications_view.html',context)


