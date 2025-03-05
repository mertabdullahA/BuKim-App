from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Users
from .serializers import UserSerializers

class KullanıcıEkle(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

class KullanıcıGüncelle(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers