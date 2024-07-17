from rest_framework import serializers
from Logro.models import Logro

class LogroSerializer(serializers.ModelSerializer):

    class Meta:

        model = Logro
        fields = '__all__'