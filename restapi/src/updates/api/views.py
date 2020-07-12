from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
import json
from .mixins import CSRFExemptMixin
from cfeapi.mixins import HttpResponseMixins
from updates.forms import UpdateModelForm
class UpdateModelDetailAPIView(View):

    def get(self,request,id,*args,**kwargs):
        json_data=UpdateModel.objects.get(id=id).serialize()
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        pass

    def put(self,request,*args,**kwargs):
        pass

    def delete(self,request,*args,**kwargs):
        pass

class UpdateModelListAPIView(HttpResponseMixins,CSRFExemptMixin,View):

    def get(self,request,*args,**kwargs):
        json_data_list=UpdateModel.objects.all().serialize()
        return HttpResponse(json_data_list,content_type='application/json')

    def post(self,request,*args,**kwargs):
        dict={
            'name':'Hamza',
            'age':34
        }
        json_data=json.dumps(dict)
        form=UpdateModelForm(request.POST)

        if form.is_valid():
            obj=form.save(commit=True)
            obj_data=obj.serialize()
            return self.render_to_response(obj_data,status=201)

        if form.errors:
            data=json.dumps(form.errors)
            return self.render_to_response(data,status=400)

        data={'message':'Not Allowed'}
        return self.render_to_response(json_data)

    def put(self,request,*args,**kwargs):
        pass

    def delete(self,request,*args,**kwargs):
        dict={'error':'You cant delete complete list'}
        res=json.dumps(dict)
        return self.render_to_response(res,403)


