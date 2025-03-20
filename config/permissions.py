from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
import logging

logger = logging.getLogger(__name__)


class TrustMeBroAuthentication(BaseAuthentication):

    def authenticate(self, request):
        username = request.headers.get("Trust-Me")
        print(username)
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)  # rule이니까
        except User.DoesNotExist:
            raise AuthenticationFailed(f"no users {username}")


class UsernameAuthentication(BaseAuthentication):

    def authenticate(self, request):
        username = request.headers.get("X-USERNAME")
        print(username)
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)  # rule이니까
        except User.DoesNotExist:
            raise AuthenticationFailed(f"no users {username}")
