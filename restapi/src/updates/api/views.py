from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse

class UpdateModelDetailAPIView(View):

    def get(self,request,*args,**kwargs):
        json_data=UpdateModel.objects.get(id=1).serialize()
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        pass

    def put(self,request,*args,**kwargs):
        pass

    def delete(self,request,*args,**kwargs):
        pass

class UpdateModelListAPIView(View):

    def get(self,request,*args,**kwargs):
        json_data_list=UpdateModel.objects.all().serialize()
        return HttpResponse(json_data_list,content_type='application/json')

    def post(self,request,*args,**kwargs):
        pass

    def put(self,request,*args,**kwargs):
        pass

    def delete(self,request,*args,**kwargs):
        pass


