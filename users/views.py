from django.http import Http404
from django.http.response import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from users.models import CustomUser as User
import json


@api_view(['POST'])
@permission_classes([AllowAny])
def user_register(request):
    body = json.loads(request.body)
    email = body['email']
    is_user = User.objects.filter(email__exact=email).count()
    if is_user == 0:
        try:
            user = User(
                email=body['email'],
            )
            user.set_password(body['password'])
            user.is_verified = False
            user.is_staff = False
            user.is_active = False
            user.save()
            return JsonResponse({'message': 'register successfully'}, status=status.HTTP_200_OK)
        except:
            JsonResponse({'message': 'user model goes wrong'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'message': 'user already existed'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def user_verify(request, user_id):

    try:
        user = User.objects.get(pk=user_id, is_verified=False)
    except:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.save()
    return JsonResponse({'message': 'verified successfully'}, status=status.HTTP_200_OK)
