from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializer import RegistrationSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'reqstatus': 'success'
        })



@api_view(['POST', ])
#@permission_classes([IsAuthenticated,]) #"detail": "Authentication credentials were not provided.
def logout_user(request):
    try:
        # get the token coming from url

        userTok = request.headers.get('Authorization')
        tokenarr = userTok.split()

        # find object
        tokobj = Token.objects.get(key=tokenarr[1])

        # delete entry for it
        tokobj.delete()

        return Response({'status': 'success', 'message': 'user logged out!'})
    except:
        return Response({'status': 'failed', 'message': 'something went wrong!'})



@api_view(['POST', ])
@permission_classes([])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        token = Token.objects.get(user=account).key

        data['status']= 'success'
        data['response'] = 'registered successfully!'
        data['email'] = account.email
        data['username'] = account.username
        data['token']=token
    else:
        data = serializer.errors
    return Response(data)