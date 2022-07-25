from django.urls import path

from api.views import Booking, Registration,CarListApi

urlpatterns = [
    path("add_car/",Registration.as_view(),name="add_car"),
    path("book/",Booking.as_view(),name="book"),
    path("",CarListApi.as_view(),name="car_list")
]