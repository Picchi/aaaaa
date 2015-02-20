from django.shortcuts import render

# Create your views here.
def index(req):
	return render(req,'aste_core/index.html')
	
def kk(req,str):
	print(str)
	print('dsa')
	return render(req,'aste_core/kk.html',{'ll':str})

