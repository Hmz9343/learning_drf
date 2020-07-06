from django.conf.urls import url
from updates.api.views import UpdateModelDetailAPIView, UpdateModelListAPIView
urlpatterns = [
    url(r'^data/',UpdateModelDetailAPIView.as_view()),
    url(r'^list/',UpdateModelListAPIView.as_view()),
]

