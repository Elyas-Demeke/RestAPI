from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer


@api_view(['POST'], )
def registration_view(request):

    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'Successfully registered the new user'
        data['email'] = account.email
        data['username'] = account.username
        data['token'] = Token.objects.get(user=account).key
    else:
        data = serializer.errors
    return Response(data)

