from django.shortcuts import render
from style_echo import settings
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {'name':'home'})

def contact(request):
	if request.method == "POST":
		subject = request.POST['message-name']
		message = request.POST['message']
		message_email = request.POST['message-email']
		to_email = "styleechoinc@gmail.com"

		# send an email
		msg = "Message: " + message + "\n" + "From:" + " " +message_email 

		send_mail(subject, msg, settings.EMAIL_HOST_USER, [to_email], fail_silently = False,)
			    		
		return render(request, 'contact.html', {'subject': subject})
	else:
		return render(request, 'contact.html', {})

