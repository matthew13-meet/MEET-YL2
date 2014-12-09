from django.shortcuts import render
from django.http import HttpResponse

from models import Poll, Choice
# Create your views here(functions) here.
#Remember each function/view the first argument/input has to be request
def index(request):
	return render(request,'firstcslecture.html',{"my_poll_num": poll_id}