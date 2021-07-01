from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import ApiSerializer
from .models import Api
from .permissions import IsRaterOrReadOnly


class ApiList(ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer


class ApiDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsRaterOrReadOnly,)
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
