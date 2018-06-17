from house.views import (
    VList,
    vEmail,
    VConfirm,
)

from django.urls import path 
app_name="house"

urlpatterns = [
  path('', VList.as_view(), name="list"),
  path('send/<to>', vEmail, name="send"),
  path('confirm-email/', VConfirm.as_view(), name="confirm")
]
