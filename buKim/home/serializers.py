from rest_framework import serializers
from .models import Users

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def validate_sayfa(self, SAYI):
        if SAYI <= 0:
            raise serializers.ValidationError("Eksik bilgi girdiniz!")
        return SAYI