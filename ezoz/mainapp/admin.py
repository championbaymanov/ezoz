from django.contrib import admin
from .models import *




class BackgroundAdmin(admin.ModelAdmin):
    list_display = ['id', 'video']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'video']

class FirstSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'pictures']

class SecondSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'pictures']

class FirstCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'thik_font', 'thin_font']

class SecondCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'thik_font', 'thin_font']

class CentralPictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'central_picture']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'pictures']


class MainNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone']

class NumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone']



# admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Background, BackgroundAdmin)

admin.site.register(Video, VideoAdmin)
admin.site.register(FirstSlider, FirstSliderAdmin)
admin.site.register(SecondSlider, SecondSliderAdmin)
admin.site.register(FirstComment, FirstCommentAdmin)
admin.site.register(SecondComment, SecondCommentAdmin)
admin.site.register(CentralPicture, CentralPictureAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(MainNumber, MainNumberAdmin)
admin.site.register(Number, NumberAdmin)
