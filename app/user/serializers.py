"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializers for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'password']
        extra_fields = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
