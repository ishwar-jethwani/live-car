from django.urls import path

from api.views import *

urlpatterns = [
    path("add_car/",Registration.as_view(),name="add_car"),
    path("book/",Booking.as_view(),name="book"),
    path("",CarListApi.as_view(),name="car_list"),
    path("detail/<str:pk>/",CarDetailView.as_view(),name="car_detail"),
    path("update/<str:pk>/",CarUpdateView.as_view(),name="update_car"),
    path("delete/<str:pk>/",CarDeleteView.as_view(),name="delete_car")



]