from .models import Account
from .serializers import AccountSerializer, LoginSerializer
from rest_framework.views import APIView, Request, Response
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class FirstLoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if not user:
            return Response(
                {"detail": "No active account found with the given credentials"},
                status=401,
            )
        refresh = RefreshToken.for_user(user)
        token_data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(token_data)

class ListCreateAccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
