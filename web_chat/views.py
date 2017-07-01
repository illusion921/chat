# _*_coding:utf-8_*_
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from chat import settings
import models
import Queue
from django.core.exceptions import ObjectDoesNotExist
import utils,datetime
import json
from django import forms
import os
import sys

# Create your views here.
reload(sys)
sys.setdefaultencoding('utf-8')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
gloab_msg_data = {}
gloab_signal = {
    'singal':{},
    'group':{},
    'file':{},
}

def Index(request):
    if request.user.is_authenticated():
        get_user = request.user.userprofile
        user_obj = models.UserProfile.objects.get(name=get_user)
        group_obj = models.ChatGroup.objects.filter(members=user_obj)
        return render(request,'index.html',{'group_all':group_obj})
    else:
        return render(request,'login.html')

def Login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {
                'login_err': "Wrong username or password!"
            })


def Register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('password-again')
        if password != password_again :
            return render(request, 'register.html', {
                'register_err': "密码两次输入不一致"
            })
        else:
            if models.User.objects.filter(username=username) or models.User.objects.filter(email=email) :
                return render(request, 'register.html', {
                    'register_err': "用户名或邮箱已经注册"
                })
            else:
                #user_obj = models.UserProfile.objects.create()
                register_obj = models.User(username=username, password=password,email=email)
                register_obj.save()
                user_obj = models.User.objects.get(username = username)
                userprofile_obj = models.UserProfile(user=user_obj,name=username)
                userprofile_obj.save()
                u = models.User.objects.get(username__exact=username)
                u.set_password(password)
                u.save()
                success = "<a href='/login'>注册成功！！点击跳转到登录页面</a>"
                return HttpResponse(success)

def Quit(request):
    logout(request)
    success = "<a href='/login'>退出成功！！点击跳转到登录页面</a>"
    return HttpResponse(success)






def Upload(request):

    msg_data=request.POST.get('data')
    msg_data = json.loads(msg_data)
    if msg_data:

        msg_data['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if msg_data.get('type')=='single':

            d1 = models.UserProfile.objects.get(id=msg_data['from_id'])
            d2 = models.UserProfile.objects.get(id=msg_data['to_id'])
            #print type(d1), '---->', d2
            models.ChatRecord.objects.create(user_id=d1.id, to_user_id=d2.id, send_type=msg_data['type'],
                                             msg_data=msg_data['msg'],record_time=msg_data['date'])

            if not gloab_msg_data.has_key(msg_data['to_id']):
                gloab_msg_data[str(msg_data['to_id'])]=utils.chat_handle()
            gloab_msg_data[str(msg_data['to_id'])].queue.put(msg_data)



        else:
            group_id = msg_data['to_id']
            group_obj = models.ChatGroup.objects.get(id=group_id)
            for member in group_obj.members.select_related():
                if not gloab_msg_data.has_key(member.id):
                    gloab_msg_data[str(member.id)]=utils.chat_handle()
                gloab_msg_data[str(member.id)].queue.put(msg_data)



    return HttpResponse('sned msg success')


def GetMsg(request):
    new_msgs = []
    uid = request.GET.get('get_id')

    if uid:
        try :
            user_obj = models.UserProfile.objects.get(id=uid)
            if not gloab_msg_data.has_key(str(user_obj.id)):
                gloab_msg_data[str(user_obj.id)]=utils.chat_handle()
            new_msgs = gloab_msg_data[str(user_obj.id)].get_msg(request)
        except ObjectDoesNotExist,e:
            print str(e)


    return HttpResponse(json.dumps(new_msgs))




def SendImg(request):
    if request.method == "POST":
        gloab_msg_data['signal'] = {}
        print request.POST.get('user')
        userq = request.POST.get('user')
        signal_name = models.UserProfile.objects.get(name=request.POST.get('to_user'))
        #relation = request.POST.get('user') + '-->' + request.POST.get('to_user')
        form_data = {
            'to_user': models.UserProfile.objects.get(name=request.POST.get('to_user')),
            'user' : models.UserProfile.objects.get(name=userq.strip()),
            'msg_img' : '',
            'file_name': '',
        }
        img_obj = models.SengImg(**form_data)
        img_obj.save()

        upload_dir = os.path.join(BASE_DIR,'statics','files')
        file_obj = request.FILES.get('file')
        #print '-->', dir(file_obj)
        with open('%s/%s' % (upload_dir, file_obj.name), 'wb') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        img_obj.msg_img = 'files/%s' % file_obj.name
        img_obj.file_name = file_obj.name
        img_obj.save()
        aa='你的好友' + str(signal_name.name) + '发来了一个文件！！！'
        gloab_msg_data['signal'][signal_name.id] = aa
        print gloab_msg_data['signal'][signal_name.id]

    return HttpResponseRedirect('/')

def Search(request):
    result = []
    #print request.POST.get('data')

    search_data = json.loads(request.POST.get('data'))
    search = search_data['search_data']
    #print type(search_data)
    if search_data['type'] == 'single':
        if search.isdigit():

            user_obj = models.UserProfile.objects.get(id = int(search))
            result = user_obj.name

        else:
            user_obj = models.UserProfile.objects.filter(name__contains = search)
            for i in range(user_obj.count()):
                result.append(user_obj[i].name)
    else:
        if search.isdigit():

            group_obj = models.ChatGroup.objects.get(id=int(search))
            result = group_obj.group_name
            print group_obj.group_name

        else:
            group_obj = models.ChatGroup.objects.filter(group_name__contains=search)
            for i in range(group_obj.count()):
                result.append(group_obj[i].group_name)
                print group_obj[i].group_name
    return HttpResponse(json.dumps(result))


def AddFriend(request):
    #print request.POST.get('data')
    add_data = request.POST.get('data')
    #print add_data
    add_data = json.loads(add_data)
    if add_data['type'] == 'single':
        from_obj = models.UserProfile.objects.get(name=add_data['name'])
        add_name = add_data['add_name']
        add_obj = models.UserProfile.objects.get(name=add_name.strip())
        if from_obj in add_obj.friends.all():
            return HttpResponse('他已经是你的好友了！！！')
        else:
            aa = {
                'user':from_obj,
                'add_user':add_obj,
                'type':add_data['type']
            }

            if not models.Confirm.objects.filter(user=from_obj,add_user=add_obj):
                confirm_obj = models.Confirm(**aa)
                confirm_obj.save()
            else:
                confirm_obj = models.Confirm.objects.get(user=from_obj,add_user=add_obj)
                confirm_obj.is_new = True
                confirm_obj.save()
            return HttpResponse('已发出请求')
    else:
        add_name = add_data['add_name']
        from_obj = models.UserProfile.objects.get(name=add_data['name'])
        add_obj = models.ChatGroup.objects.get(group_name=add_name.strip())
        if from_obj in add_obj.members.all():
            return HttpResponse('你已经在群组里了！！！')
        else:
            add_obj.members.add(from_obj)
            return HttpResponse('success')


def Record(request):
    get_user = request.user.userprofile
    user_obj = models.UserProfile.objects.get(name=get_user)
    msg_list = user_obj.to_user_record.all().order_by('record_time')
    a = {

    }
    for i in msg_list:
        if not a.has_key(i.user.name):
            a[i.user.name] = {}
            a[i.user.name][i.record_time] = i.msg_data.strip()
        else:
            a[i.user.name][i.record_time] = i.msg_data.strip()
    if request.method == "GET":
        return render(request,'chat_record.html',{'data':a})
    else:
        post_user = request.POST.get('data')
        user = json.loads(post_user)
        return HttpResponse(json.dumps(a[user]))


def ChatImg(request):
    get_user = request.user.userprofile
    img_obj = models.SengImg.objects.filter(to_user=get_user).order_by('-add_time')
    return render(request,'chat_img.html',{'data':img_obj})



def ChatGroup(request):
    if request.method == 'GET':
        return render(request,'chat_group.html')
    else:

        funder = request.user.userprofile
        print funder
        group_name = request.POST.get('groupname')
        user_obj = models.UserProfile.objects.get(name=funder)
        create_obj = models.ChatGroup(group_name=group_name,founder=user_obj)
        create_obj.save()
        add_obj = models.ChatGroup.objects.get(group_name=group_name)
        add_obj.members.add(user_obj)
        add_obj.admins.add(user_obj)
        add_obj.save()

        return HttpResponse('success')



def ChgPwd(request):
    if request.method == 'GET':
        return render(request,'chg_pwd.html')
    else:
        username = request.user
        old_pwd = str(request.POST.get('oldpwd'))
        new_pwd = str(request.POST.get('newpwd'))
        new_pwd_again = request.POST.get('newpwdagain')

        if new_pwd != new_pwd_again:
            signal = '两次输入的密码不一致！！！'
            return render(request,'chg_pwd.html',{'error':signal})
        else:
            u = models.User.objects.get(username__exact=username)
            u.set_password(new_pwd)
            u.save()
            success = "<a href='/login'>修改成功！！点击跳转到登录页面</a>"
            return HttpResponse(success)



def Confirm(request):
    confirmdata = {}
    uid = request.GET.get('get_id')
    add_obj = models.UserProfile.objects.get(id=uid)
    confirm_obj = models.Confirm.objects.filter(add_user=add_obj)
    if confirm_obj:
        for i in confirm_obj:
            #print i.status
            if not i.status:
                aa={
                    'user':i.user.name,
                    'add_user':i.add_user.name,
                    'type':i.type,
                    'status':i.status,
                    'is_new':i.is_new
                }
                confirmdata[i.user.name] = aa
                i.is_new = False
                i.save()
        #print confirmdata
        bb = json.dumps(confirmdata)
        #print type(bb)
        #print bb
        return HttpResponse(bb)
    else:
        return HttpResponse('NO')

def AddSignal(request):
    add_data = request.POST.get('data')
    # print add_data
    add_data = json.loads(add_data)
    #print add_data
    user_obj = models.UserProfile.objects.get(name=add_data['user'])
    add_name = add_data['add_user']
    add_obj = models.UserProfile.objects.get(name=add_name.strip())
    #print user_obj,add_obj
    confirm_obj = models.Confirm.objects.get(user=user_obj,add_user=add_obj)
    confirm_obj.status = True
    confirm_obj.save()
    user_obj.friends.add(add_obj)

    return HttpResponse('success')

def Refuse(request):
    add_data = request.POST.get('data')
    add_data = json.loads(add_data)
    user_obj = models.UserProfile.objects.get(name=add_data['user'])
    add_name = add_data['add_user']
    add_obj = models.UserProfile.objects.get(name=add_name.strip())
    # print user_obj,add_obj
    confirm_obj = models.Confirm.objects.get(user=user_obj, add_user=add_obj).delete()
    return HttpResponse('已拒绝！！！')

def DelUser(request):
    add_data = request.POST.get('data')
    add_data = json.loads(add_data)
    user_obj = models.UserProfile.objects.get(name=add_data['user'])
    del_name = add_data['del_user']
    del_obj = models.UserProfile.objects.get(name=del_name.strip())
    # print user_obj,add_obj
    del_obj = user_obj.friends.remove(del_obj)
    return HttpResponse('已删除！！！')