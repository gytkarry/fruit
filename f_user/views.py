from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha1   #加密模块
from f_user.models import User,Address
from f_goods.models import GoodInfo
from f_user import user_decorator

# Create your views here.
def login(request):
    uname=request.COOKIES.get('uname','')
    pwd=request.COOKIES.get('upwd','')
    context={'uname':uname,'pwd':pwd,'error':0}
    try:
        url=request.META['HTTP_REFERER']
        if '/user/register' in url:raise Exception()
    except:url='/'
    response=render(request, 'f_user/login.html', context)
    response.set_cookie('url',url)
    return response

def register(request):
    return render(request,'f_user/register.html')

@user_decorator.login
def shdz(request):
    adds=Address.objects.filter(uid=request.session.get('uid', ''),scbz=0)
    return render(request,'f_user/shdz.html',locals())

def login_handle(request):
    post=request.POST#接收表单请求
    uname=post.get('username')
    pwd=post.get('pwd','')
    remember=post.get('remember','0')
    s=sha1()
    s.update(pwd.encode('utf8'))   #先编码
    upwd=s.hexdigest()      #十六进制编码
    user=User.objects.filter(uname=uname).filter(upwd=upwd).first()
    if user:
        url=request.COOKIES.get('url','/')
        red=HttpResponseRedirect(url)
        if remember=='1':
            red.set_cookie('uname',uname.encode('utf-8'))
            red.set_cookie('upwd',pwd)
        else:
            red.set_cookie('uanme','',max_age=-1)
            red.set_cookie('upwd','',max_age=-1)
        request.session['username']=uname
        request.session['uid']=user.id
        return red
    else:
        context={'error':1,'uname':uname}
        return render(request,'f_user/login.html',context)

def register_handle(request):
    post = request.POST   # 接收用户输入
    # unum=post.get('unum','')
    uname = post.get('username','')
    pwd = post.get('pwd','')
    cpwd = post.get('cpwd','')
    uemail = post.get('email','')
    if pwd != cpwd:
        return redirect('/user/register')
    # 密码加密
    # 使用sha1加密
    s1 = sha1()
    s1.update(pwd.encode('utf8'))   # sha1加密前，要先编码为比特
    pwd = s1.hexdigest()
    user = User()  # 存入数据库
    user.uname = uname
    user.upwd = pwd
    user.uemil = uemail
    user.save()
    print(user.uname)
    return redirect('/user/login')

def logout(request):
    request.session.flush()   #清空session中所有信息
    return redirect('/')

def register_exist(request):
    uname=request.GET.get('un')
    count= User.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

@user_decorator.login
def user_center_info(request):
    username=request.session.get('username','')
    user=User.objects.filter(uname=username).first()
    goodids=request.COOKIES.get('goodids','')
    goods_list = []
    if goodids!='':
        goodidl=goodids.split(',')
        for i in goodidl:
            goods_list.append(GoodInfo.objects.filter(pk=i).first())
            pass
    return render(request,'f_user/user_info.html',locals())

@user_decorator.login
def userupdate(request):
    post = request.POST
    uid=request.session.get('uid','')
    user=User.objects.filter(id=uid).first()
    user.uname=post.get('un','')
    user.uphone = post.get('uphone', '')
    user.uemail = post.get('uemil', '')
    user.usex = post.get('usex', '')
    user.save()
    request.session['username']=user.uname
    return redirect('/')

@user_decorator.login
def add_save(request):
    post = request.POST
    aid=post.get('aid')
    print(aid)
    if aid:
        Address.objects.filter(id=aid).update(reciver = post.get('reciver'),sheng = post.get('sheng'),shi= post.get('shi'),
                                              qu=post.get('qu'),detialaddr= post.get('detialaddr'),
                                              yzbm= post.get('yzbm'),rphone= post.get('rphone'))
    else:Address.objects.create(reciver = post.get('reciver'),sheng = post.get('sheng'),shi= post.get('shi'),
                                              qu=post.get('qu'),detialaddr= post.get('detialaddr'),
                                              yzbm= post.get('yzbm'),rphone= post.get('rphone'),uid=request.session['uid'])
    return redirect('/')

@user_decorator.login
def mrdz(request):
    dzid=request.GET.get('dzid')
    Address.objects.all().update(mrdz=0)
    Address.objects.filter(id=dzid).update(mrdz=1)
    return redirect('/user/shdz')

@user_decorator.login
def scdz(request):
    dzid=request.GET.get('dzid')
    Address.objects.filter(id=dzid).update(scbz=1)
    return redirect('/user/shdz')

@user_decorator.login
def bjdz(request):
    dzid=request.GET.get('dzid')
    add=Address.objects.get(id=dzid)
    adds = Address.objects.filter(uid=request.session.get('uid', ''), scbz=0)
    return render(request, 'f_user/shdz.html', locals())