from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        account = serializer.save()

        token = Token.objects.get(user=account)

        data = {
            'response': 'Registration successful!',
            'username': account.username,
            'email': account.email,
            'token': token.key
        }
        return Response(data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
