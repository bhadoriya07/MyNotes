from django.shortcuts import render , redirect
from notesapp.models import text

# Create your views here.

def newnote(request):
	if request.session.has_key('email'):
		if request.method == "POST":
			note = request.POST['note']
			username = request.user.first_name #geeting first_name from User table
			upload = text(Uname=username,content=note)#assigning value to Uname and content in text table
			upload.save()
			data = text.objects.filter(Uname=username)#filtering the content according to the username in text table
			context = {
				'Uname':username,
				'data':data,
			}
			return render(request, 'notesapp/main.html',context)
		else:
			username = request.user.first_name
			data = text.objects.filter(Uname=username)
			context = {
				'Uname': username,
				'data': data,
			}
			return render(request,'notesapp/main.html',context)
	else:
		data={'error':"Please Login First"}
		return render(request,'notesapp/login.html',data)
