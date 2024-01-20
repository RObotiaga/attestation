from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, \
    UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser
from .serializers import CustomUserSerializer, \
    UserRegisterSerializer, CustomUserUpdateSerializer
from django.core.mail import send_mail
from django.urls import reverse
from config import settings
import secrets


class RegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=False)
        token = secrets.token_urlsafe(nbytes=8)
        user.token = token
        activate_url = reverse('users:confirm_mail',
                               kwargs={'token': user.token})
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения регистрации \
            перейдите по ссылке: http://localhost:8000/{activate_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )
        user.save()


class ProfileAPIView(UpdateAPIView):
    serializer_class = CustomUserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class DeleteProfileAPIView(DestroyAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class SendNewPasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        new_password = secrets.token_hex(nbytes=8)
        send_mail(
            subject='Вы сменили пароль',
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email]
        )
        request.user.set_password(new_password)
        request.user.save()
        return Response(status=status.HTTP_200_OK)
