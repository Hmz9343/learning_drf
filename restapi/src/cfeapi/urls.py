"""cfeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from updates.views import (
            json_get_example,
            jsonCBV,
            jsonCBV2,
            SerializeDetailView,
            SerializedListView
    )


urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^json/example/',json_get_example),
    url(r'^api/updates/',include('updates.api.urls'))
    #url(r'^json/cbv2',jsonCBV2.as_view()),
    #url(r'^json/cbv/',jsonCBV.as_view()),
    #url(r'^serialized/data/',SerializeDetailView.as_view()),
    #url(r'^serializedlist/data',SerializedListView.as_view()),
]
