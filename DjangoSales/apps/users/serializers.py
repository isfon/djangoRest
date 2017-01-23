from rest_framework import routers, serializers, viewsets, generics
from rest_framework.response import Response
from .models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name','tipo')


class TokenSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Token
        fields = ('key', 'user')

class TokenViewSet(viewsets.ModelViewSet):

    queryset = Token.objects.all()
    serializer_class = TokenSerializer
