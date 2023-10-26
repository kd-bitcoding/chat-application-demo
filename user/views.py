# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Import models
from user.renderers import UserRenderer

# Import serializers
from user.serializers import UserProfileSerializer


class UserProfileAPIView(APIView):
    '''
    User Profile API View
    '''
    renderer_class = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

user_profile_view = UserProfileAPIView.as_view()