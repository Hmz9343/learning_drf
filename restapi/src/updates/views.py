import json
from django.shortcuts import render
from .models import Update
from django.http import JsonResponse,HttpResponse
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
from .models import Update
from django.core.serializers import serialize

def json_get_example(request):
    #GET Request
    data={
        "count":1,
        "name":"Hamza"
    }
    json_data=json.dumps(data)
    #return JsonResponse(data)
    return HttpResponse(json_data,content_type='application/json')

# Create your views here.



class jsonCBV2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data={
            "name":"Hamza",
            "Age":23
        }
        return self.render_to_json_response(data)

class jsonCBV(View):

    def get(self,request,*args,**kwargs):
        data={
        "count":2,
        "name":"Hamza Aqeel"
        }
        return JsonResponse(data)

class SerializeDetailView(View):
    def get(self,request,*args,**kwargs):
        obj = Update.objects.get(id=1)
        data=serialize("json",[obj,],fields=('user','content'))
        return HttpResponse(data,content_type='application/json')

class SerializedListView(View):
    def get(self,request,*args,**kwargs):
        obj=Update.objects.all();
        data=serialize("json",obj,fields=('user','content'))
        print(data)
        #json_data=json.dumps(data)
        return HttpResponse(data,content_type='application/json')

