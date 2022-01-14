from django.db.models import fields
from rest_framework import serializers
from .models import *


# class RestaurantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Restaurant
#         fields = '__all__'


class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class FirstSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstSlider
        fields = '__all__'


class SecondSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondSlider
        fields = '__all__'


class FirstCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstComment
        fields = '__all__'


class SecondCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondComment
        fields = '__all__'


class CentralPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralPicture
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class MainNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainNumber
        fields = '__all__'


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'