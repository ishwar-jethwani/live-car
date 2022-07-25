from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.permissions import *
from .models import *
from .serializers import *

class Registration(CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = CarOwnerSerializer

class Booking(CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = BookingSerializer

class CarListApi(ListAPIView):
    serializer_class = CarOwnerSerializer
    def get_queryset(self):
        if "location" in self.request.query_params:
            location = self.request.query_params["location"]
            objs = Movement.objects.filter(start_point__icontains=location)
            queryset = []
            for obj in objs:
                queryset.append(obj.car)
        else:
            queryset = CarOwner.objects.all()
        return queryset

            

        








