from rest_framework import serializers
from accounts.models import Account
from rest_framework.validators import UniqueValidator

class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=Account.objects.all(),
                message="user with this email already exists.",
            )
        ],
    )
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)