from rest_framework.serializers import ModelSerializer
from .models import *

class CarOwnerSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CarOwner


class BookingSerializer(ModelSerializer):
    class Meta:
        fields = ["car","start_point","destination","start_time","end_time"]
        model = Movement
        depth = 1
