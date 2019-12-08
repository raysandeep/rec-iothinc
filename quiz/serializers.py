from .models import SN
from rest_framework import serializers





class SNSerializer(serializers.ModelSerializer):
    class Meta:
        model = SN
        fields = '__all__'