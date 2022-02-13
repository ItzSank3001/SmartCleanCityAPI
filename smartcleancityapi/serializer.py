from rest_framework import serializers
from .models import User, Bin, Complaint

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = '__all__'

class BinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bin
        fields = '__all__'

