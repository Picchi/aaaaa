from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
import datetime
import random
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Message

@login_required
def index(req):
	try:
		o=Message.objects.filter(Q(From=req.user)|Q(To=req.user)).order_by('data')[:5]
	except Exception as e:
		print(e)
		o=()
	print(o)	#o=Oggetto.objects.filter(data_termine__gt=datetime.datetime.now()).order_by('nome')[:5]
	return render(req,'message/index.html',{'o':o})
