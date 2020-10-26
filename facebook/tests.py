from django.test import TestCase
from django.shortcuts import render
# Create your tests here.


def Home():
	return render(request, 'home.html', {})


