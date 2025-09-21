from random import choices

from rest_framework import serializers

from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ('email','password')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'middle_name')


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)


class AdminChangePermissionSerializer(serializers.Serializer):

    role = serializers.CharField(required=True)
    CHOICES =['can_delete','can_edit','can_view','can_view_all','can_delete_all','can_edit_all']
    perms = serializers.DictField(child=serializers.BooleanField(),required=True)

    def validate_perms(self,value):
        for perm in value:
            if perm not in self.CHOICES:
                raise serializers.ValidationError(f"Передан Неверный ключ {perm}")

        return value