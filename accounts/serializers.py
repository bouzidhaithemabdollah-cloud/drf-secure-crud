from rest_framework import serializers
from .models import Ohmy 

class  OhmySerializer(serializers.ModelSerializer):
    class Meta :
        model=Ohmy
        fields =['id' , 'name' ,'email','password']
        extra_kwargs = {
            'password' :{'write_only':True}
        }
    def create(self,validated_data):
        email=validated_data['email']
        name=validated_data['name']
        password=validated_data['password']
        user=Ohmy.objects.create_user(email=email ,name=name , password= password)
        return user