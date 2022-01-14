from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import render


# class RestaurantCreateApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer



# class RestaurantListApiView(generics.ListCreateAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer


class BackgroundCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer



class BackgroundListApiView(generics.ListCreateAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer


class VideoCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



class VideoListApiView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class FirstSliderCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FirstSlider.objects.all()
    serializer_class = FirstSliderSerializer



class FirstSliderListApiView(generics.ListCreateAPIView):
    queryset = FirstSlider.objects.all()
    serializer_class = FirstSliderSerializer


class SecondSliderCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SecondSlider.objects.all()
    serializer_class = SecondSliderSerializer



class SecondSliderListApiView(generics.ListCreateAPIView):
    queryset = SecondSlider.objects.all()
    serializer_class = SecondSliderSerializer


class FirstCommentCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FirstComment.objects.all()
    serializer_class = FirstCommentSerializer



class FirstCommentListApiView(generics.ListCreateAPIView):
    queryset = FirstComment.objects.all()
    serializer_class = FirstCommentSerializer


class SecondCommentCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SecondComment.objects.all()
    serializer_class = SecondCommentSerializer



class SecondCommentListApiView(generics.ListCreateAPIView):
    queryset = SecondComment.objects.all()
    serializer_class = SecondCommentSerializer



class CentralPictureCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CentralPicture.objects.all()
    serializer_class = CentralPictureSerializer


class CentralPictureListApiView(generics.ListCreateAPIView):
    queryset = CentralPicture.objects.all()
    serializer_class = CentralPictureSerializer


class GalleryCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryListApiView(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer






class MainNumberCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainNumber.objects.all()
    serializer_class = MainNumberSerializer


class MainNumberListApiView(generics.ListCreateAPIView):
    queryset = MainNumber.objects.all()
    serializer_class = MainNumberSerializer


class NumberCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer


class NumberListApiView(generics.ListCreateAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
