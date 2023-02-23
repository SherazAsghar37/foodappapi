from api.models import CustomUser, Food,Products
from rest_framework import serializers
from django.contrib.auth import get_user_model
class ProductSerializer(serializers.ModelSerializer):
    # related_id = serializers.ReadOnlyField()
    class Meta:
        model=Products
        # fields=['id','name','description','price','stars','img','location','created_at','updated_at','type_id']
        fields='__all__'
class FoodSerailizer(serializers.ModelSerializer):
    # id = ProductSerializer(read_only=True,many=True)
    products = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Food
        fields = ['total_size','type_id','offset','products']
        # fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name','password','phone','email']
        
    def create(self,validated_data):
        user = get_user_model().objects.create(email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user