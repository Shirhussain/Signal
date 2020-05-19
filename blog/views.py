from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver



def khana(request):
	return HttpResponse("here is somthing in HttpResponse")


@receiver(request_finished)
def post_request_receiver	(sender,**kwargs):
	print("request fineshed")