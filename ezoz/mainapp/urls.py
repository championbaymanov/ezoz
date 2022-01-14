from django.urls import path
from . import views


urlpatterns = [
    # path("restaurant", views.RestaurantListApiView.as_view()),
    # path("restaurant/<int:pk>", views.RestaurantCreateApiView.as_view()),

    path('background', views.BackgroundListApiView.as_view()),    
    path('background/<int:pk>', views.BackgroundCreateApiView.as_view()),

    path('video', views.VideoListApiView.as_view()),    
    path('video/<int:pk>', views.VideoCreateApiView.as_view()),
    
    path('first_slider', views.FirstSliderListApiView.as_view()),    
    path('first_slider/<int:pk>', views.FirstSliderCreateApiView.as_view()),
    
    path('second_slider', views.SecondSliderListApiView.as_view()),    
    path('second_slider/<int:pk>', views.SecondSliderCreateApiView.as_view()),
    
    path('first_comment', views.FirstCommentListApiView.as_view()),    
    path('first_comment/<int:pk>', views.FirstCommentCreateApiView.as_view()),
    
    path('second_comment', views.SecondCommentListApiView.as_view()),    
    path('second_comment/<int:pk>', views.SecondCommentCreateApiView.as_view()),

    path('central_picture', views.CentralPictureListApiView.as_view()),    
    path('central_picture/<int:pk>', views.CentralPictureCreateApiView.as_view()),
    
    path('gallery', views.GalleryListApiView.as_view()),    
    path('gallery/<int:pk>', views.GalleryCreateApiView.as_view()),

    path('main_number', views.MainNumberListApiView.as_view()),    
    path('main_number/<int:pk>', views.MainNumberCreateApiView.as_view()),
    
    path('number', views.NumberListApiView.as_view()),    
    path('number/<int:pk>', views.NumberCreateApiView.as_view()),

]