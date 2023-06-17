from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework import viewsets


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


class RegistrationView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = RegistrationSerializer


#
class PharmacyRegistration(generics.CreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
#
class CustomerRegistration(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
#
@api_view(['GET'])
def branch_cities(request,branch):
    details=City.objects.filter(branch__id=branch)
    data=CitySerializer(details,many=True).data
    return Response({'data':data})
#
@api_view(['GET'])
def city_customer(request,city):
    details=Customer.objects.filter(city__id=city)
    data=CustomerDetailsSerializer(details,many=True).data
    return Response({'data':data})
#
@api_view(['GET'])
def branch_staff(request):
    user=request.user
    details=Branch.objects.filter(staff=user)
    data=Branch_StaffSerializer(details,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def Cities(request):
    details=City.objects.all()
    data=CitySerializer(details,many=True).data
    return Response({'data':data})