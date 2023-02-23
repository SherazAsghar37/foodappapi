from rest_framework import viewsets,permissions
from api.models import Food,Products
from api.serializer import FoodSerailizer,ProductSerializer,RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
#Create your views here.
class FoodViewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Food.objects.all()
    serializer_class = FoodSerailizer
    
class ProductsViewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class Register(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    def post(self,request):
        Postserializer = RegisterSerializer(data=request.data)
        if not (Postserializer.is_valid()):
            print("Data",Postserializer.errors)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            Postserializer.save()
            User = get_user_model()
            user = User.objects.get(email = Postserializer.data['email'])
            tokenobj ,_ = Token.objects.get_or_create(user=user)
            return Response({"Token":str(tokenobj)})

# class FoodViewset(generics.ListCreateAPIView):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerailizer
# class ProductsViewset(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer