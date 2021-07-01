from rest_framework.serializers import ModelSerializer
from .models import Api


class ApiSerializer(ModelSerializer):
    class Meta:
        model = Api
        fields = ("id", "name", "rater", "rating")
