from django.http import JsonResponse
from django.http import HttpResponse
class JsonResponseMixin(object):

    def render_to_json_response(self,context,**response_kwargs):
        return JsonResponse(self.get_data(context),**response_kwargs);
    def get_data(self,context):
        return context;

class HttpResponseMixins(object):

    def render_to_response(self,data,status=200):
        content_type='application/json'
        return HttpResponse(data,content_type=content_type,status=status)