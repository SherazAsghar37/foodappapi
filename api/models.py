
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser,User
from django.utils.translation import gettext_lazy as _

# Create your models here.
#creating main model
class Food(models.Model):
    total_size = models.IntegerField()
    offset  = models.IntegerField()
    type_id =models.IntegerField()
    
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price =  models.IntegerField()
    stars =  models.IntegerField()
    img = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    type_id = models.IntegerField(default=0)
    products = models.ForeignKey(Food,on_delete=models.CASCADE,
                related_name='products')
    
class UserManager(BaseUserManager):
    use_in_migrations = True

    def  create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError(_("Email is required"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        
        user.set_password(password)
        user.save(using = self._db)
        print("called")
        return user
    def create_superuser(self,email,password,**extra_fileds):
        extra_fileds.setdefault("is_staff",True)
        extra_fileds.setdefault('is_active',True)
        extra_fileds.setdefault('is_superuser',True)
        if(extra_fileds.get('is_staff')is not True):
            raise ValueError(_("superuser must have is_staff = Ture"))
        if(extra_fileds.get('is_active')is not True):
            raise ValueError(_("superuser must have is_active = Ture"))
        if(extra_fileds.get('is_superuser')is not True):
            raise ValueError(_("superuser must have is_superuser = Ture")) 
        user = self.create_user(email,password=password,**extra_fileds)
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    
class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    is_varified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100,null=True,blank=True)
    forget_passsord = models.CharField(max_length=100,null=True,blank=True)
    
    last_login_time = models.DateTimeField(null=True,blank=True)
    last_logout_time = models.DateTimeField(null=True,blank=True)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=["phone","name"]
    objects = UserManager()
    