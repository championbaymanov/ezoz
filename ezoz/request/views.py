from rest_framework import generics
from request.serializers import RequestSerializer
from request.models import *



class RequestCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer



class RequestListApiView(generics.ListCreateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
