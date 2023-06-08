from django.http import HttpResponse, JsonResponse

from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import RegisteredAndroidUser
from .serializers import RegisteredAndroidUserSerializer

class RegisterAndroidUserApiView(APIView):
    api_name = "api-register-android-user"

    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  # Allow access to all users, authenticated or not

    def get(self, request):
        users = RegisteredAndroidUser.objects.all()

        users_serialized = RegisteredAndroidUserSerializer(users, many=True)

        json_data = JSONRenderer().render(users_serialized.data)
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(player_serialized.data, safe=False) #Above Two Lines can be written just by Using JsonResponse

    def post(self, request):
        user_serialized = RegisteredAndroidUserSerializer(data=request.data)
        if user_serialized.is_valid():
            user_serialized.save()
            return Response({'msg':'RegisteredAndroidUser Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
