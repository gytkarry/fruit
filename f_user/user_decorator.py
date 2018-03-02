from django.http import HttpResponseRedirect

def login(func):
    def login_fun(request,*args,**kw):
        if request.session.has_key('username'):
            return func(request,*args,**kw)
        else:
            red=HttpResponseRedirect('/user/login')
            red.set_cookie('url',request.get_full_path())
            return red
    return login_fun