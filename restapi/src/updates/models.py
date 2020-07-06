import json
from django.db import models
from django.conf import settings
from django.core.serializers import serialize

def upload_update_image(instance,filename):
    return "update/{user}/{filename}".format(user=instance.user,filename=filename)

class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        obj=self
        json_data=serialize('json',obj,fields=('user','content','image'))
        dic=json.loads(json_data)
        print(dic)
        json_data=json.dumps(dic[0]['fields'])
        return json_data

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model,using=self._db)

class Update(models.Model):
    user        =   models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content     =   models.TextField(blank=True,null=True)
    image       =   models.ImageField(upload_to=upload_update_image,blank=True,null=True)
    updated     =   models.DateTimeField(auto_now=True)
    timestamp   =   models.DateTimeField(auto_now_add=True)

    objects= UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        json_data = serialize('json',[self],fields=('user','content'))
        dic=json.loads(json_data)
        print(dic)
        json_data=json.dumps(dic[0]['fields'])
        return json_data

