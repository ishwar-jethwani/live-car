from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.permissions import *
from .models import *
from .serializers import *

class Registration(CreateAPIView):
    "Add Car In SIte By Car Owner"
    permission_classes = [IsAuthenticated,]
    serializer_class = CarOwnerSerializer

class Booking(CreateAPIView):
    "Booked Car For Travel By Passanger"
    permission_classes = [IsAuthenticated,]
    serializer_class = BookingSerializer

class CarListApi(ListAPIView):
    "Car List FOr Home Page"
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

class CarDetailView(RetrieveAPIView):
    "Car Detail View For Passanger"
    queryset = CarOwner.objects.all()
    serializer_class = CarOwnerSerializer
    lookup_field = "pk"

class CarUpdateView(RetrieveUpdateAPIView):
    "Car Can be Updated By Car Owner"
    serializer_class = CarOwnerSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = "pk"
    def get_queryset(self):
        user = self.request.user
        queryset = CarOwner.objects.filter(user=user)
        return queryset

class CarDeleteView(RetrieveDestroyAPIView):
    "Car Object Can be Deleted By Admin"
    serializer_class = CarOwnerSerializer
    permission_classes = [IsAdminUser]
    queryset = CarOwner.objects.all()
    lookup_field = "pk"




        

            

        








