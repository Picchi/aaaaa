from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

def logout_page(request):
    logout(request)
    print("LogOut ")
    return HttpResponseRedirect('/')

def sign_up_page(req):
	if req.user.is_authenticated():
		return HttpResponseRedirect('/')
	return render(req,'/')
	return render(req,'reg/sig_up.html')