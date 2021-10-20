# from users.models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UsersRegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(APIView):
  def post(self, request):
    serializer = UsersRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    serializer = UserSerializer(request.users)
    print(serializer)
    return Response(serializer.data)