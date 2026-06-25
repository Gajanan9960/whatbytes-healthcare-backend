from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["name", "email", "password"]

    def create(self, validated_data):
        name = validated_data.pop("name")

        user = User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            first_name=name,
            password=validated_data["password"],
        )

        return user