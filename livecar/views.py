from django.contrib.auth.models import User
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from django.core.mail import send_mail
#first ask the mobile number 
# match the mobile number with our database
# genrate otp by using random module
# send otp to mobile number by using send_mail  function
# compare otp to genrated otp



class EmailVerification(APIView):
    "Email Verification Function"
    otp = random.randint(100000,999999)
    email = ""
    def get(self,request):
        self.email = request.GET["email"]
        user = User.objects.filter(email=self.email)
        if user.exists:
            message = f"welcome to live car application this is you verification code {self.otp} please pest this code to verify your email id"
            subject = "Email Verification"
            send_mail(subject=subject,message=message,from_email=None,recipient_list=[self.email])
            return Response(data={"msg":f"we have sent mail to you for code on {self.email}"},status=status.HTTP_200_OK)
        return Response(data={"msg":"you have wrong email please register with this email first"},status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        userotp = request.data["otp"]
        self.email = request.data["email"]
        if self.otp == int(userotp):
            user = User.objects.get(email=self.email)
            obj  = CarOwner.objects.get(user=user)
            obj.verified = True
            obj.save()
            return Response(data={"msg":"your email is sucessfully verified"},status=status.HTTP_200_OK)
        return Response(data={"msg":"you have entered wrong otp"},status=status.HTTP_200_OK)
            

        


            

