from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(req):
	return render(req,'aste_core/index.html')

@login_required
def kk(req,str):
	print(req.user)
	print('dsa')
	return render(req,'aste_core/kk.html',{'ll':str})

