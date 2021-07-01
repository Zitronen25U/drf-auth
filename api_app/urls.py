
from .views import ApiList, ApiDetail
from django.urls import path

urlpatterns = [
    path("", ApiList.as_view(), name="Api_list"),
    path("<int:pk>/", ApiDetail.as_view(), name="Api_detail"),
]
