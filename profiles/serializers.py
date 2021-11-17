from rest_framework import serializers
from .models import Person
 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'FirstName', 'LastName','BirthDay','MobileNumber','Address','Gender']