from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse(render, 'audit/base.html')


def lead_list(request):
    pass


def lead_details(request, lead_id):
    return HttpResponse("You're looking at lead %s." % lead_id)


def lead_anal_results(request, lead_id):
    response = "You're looking at the results of the lead audit for lead %s."
    return HttpResponse(response % lead_id)


def contact_list(request):
    response = "Contact List"
    return HttpResponse(response)


def contact_details(request, person_id):
    return HttpResponse("You're looking at contact %s." % person_id)


def organization_list(request):
    pass


def organization_details(request):
    pass
