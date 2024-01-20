from django.urls import path
from .views import (
    RegisterAPIView,
    ProfileAPIView,
    DeleteProfileAPIView,
    SendNewPasswordAPIView
)
from .apps import UsersapiConfig
from rest_framework_simplejwt.views \
    import TokenRefreshView, TokenObtainPairView

app_name = UsersapiConfig.name

urlpatterns = [
    path('register/', RegisterAPIView.as_view(),
         name='api_register'),
    path('profile/', ProfileAPIView.as_view(),
         name='api_profile'),
    path('delete-profile/', DeleteProfileAPIView.as_view(),
         name='api_delete_profile'),
    path('send-new-password/', SendNewPasswordAPIView.as_view(),
         name='api_send_new_password'),
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
