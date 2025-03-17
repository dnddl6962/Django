from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import User
from .serializers import UserListSerializer, UserDetailSerializer


class UserList(APIView):

    def get(self, request):
        all_users = User.objects.all()
        serializer = UserListSerializer(
            all_users,
            many=True,
        )
        return Response(serializer.data)


class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
