from django.shortcuts import render
from .models import Update
from django.http import JsonResponse,HttpResponse


def update_model_detail_view(request):
    data={
        "count":1,
        "name":"Hamza"
    }
    return JsonResponse(data)
# Create your views here.
