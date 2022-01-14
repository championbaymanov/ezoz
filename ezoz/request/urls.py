from django.urls import path

from request import views

urlpatterns = [
    path('list/', views.RequestListApiView.as_view()),
    path('create/', views.RequestCreateApiView.as_view()),
]
