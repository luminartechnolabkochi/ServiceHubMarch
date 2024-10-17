from django.shortcuts import render

# Create your views here.
from rest_framework import authentication,permissions

from rest_framework import generics

from service.serializers import CustomerSerializer,WorkSerializer

from service.models import Customer,Work

from service.permissions import OwnerOnly

from django.core.mail import send_mail

class CustomerListCreateView(generics.ListCreateAPIView):

    queryset=Customer.objects.all()

    serializer_class=CustomerSerializer

    authentication_classes=[authentication.TokenAuthentication]
    # authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):
        
        return serializer.save(service_advisor=self.request.user)
    

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=CustomerSerializer

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]


    def perform_update(self, serializer):
        
        work_status=serializer.validated_data.get("work_status")

        if work_status=="completed":

            print("sending email")

        serializer.save()







class WorkCreateView(generics.CreateAPIView):

    serializer_class=WorkSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]


    def perform_create(self, serializer):
        
        id=self.kwargs.get("pk")

        cust_obj=Customer.objects.get(id=id)

        return serializer.save(customer_object=cust_obj)


class WorkUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=WorkSerializer

    queryset=Work.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]

    
