from rest_framework import serializers
from .models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class Issuebookserializer(serializers.ModelSerializer):
    class Meta:
        model = Issuebook
        fields ='__all__'