from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import uuid
#Managing the permissions 
class OhmyManager(BaseUserManager):
    def create_user(self,email,name,password=None ,**extra):
        if not email :
            raise ValueError("Email value not found please retype it !")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name,**extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password=None,**extra):
        extra.setdefault('is_staff',True)
        extra.setdefault('is_superuser',True)
        return self.create_user(email,name,password,**extra)



class Ohmy(AbstractBaseUser, PermissionsMixin):
    #todo unity
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #todo important essencial fields
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True , db_index=True , max_length=200 ,null=False)
    #todo permission & activation fields
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False )
    objects=OhmyManager()

    #todo new for me  new sys config
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email