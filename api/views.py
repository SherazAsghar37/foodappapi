from rest_framework import viewsets,permissions
from api.models import Food,Products
from api.serializer import FoodSerailizer,ProductSerializer,RegisterSerializer,UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import get_user_model,authenticate
from rest_framework.authtoken.models import Token
#Create your views here.
class FoodViewset(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes=[AllowAny]
    queryset = Food.objects.all()
    serializer_class = FoodSerailizer
    
class ProductsViewset(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
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
class Signin(APIView):
    authentication_classes=[]
    permission_classes=[AllowAny]
    def post(self,request=Request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
            return Response({"Token":str(user.auth_token.key)},status=status.HTTP_200_OK)
        else:
            return  Response(status=status.HTTP_404_NOT_FOUND)
        
class CurrentUserView(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
        
        

# class FoodViewset(generics.ListCreateAPIView):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerailizer
# class ProductsViewset(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer