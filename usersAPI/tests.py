from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from users.models import CustomUser


class ProfileAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create(email='test@example.com',
                                               password='testpassword')
        self.client.force_authenticate(user=self.user1)

    def test_update_profile(self):
        url = reverse('usersAPI:api_profile')
        data = {'field_to_update': 'new_value'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more assertions as needed


class DeleteProfileAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create(email='test@example.com',
                                               password='testpassword')
        self.client.force_authenticate(user=self.user1)

    def test_delete_profile(self):
        url = reverse('usersAPI:api_delete_profile')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure user was deleted from the database
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(email='test@example.com', )

        # Add more assertions as needed


class SendNewPasswordAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create(email='test@example.com',
                                               password='testpassword')
        self.client.force_authenticate(user=self.user1)

    def test_send_new_password(self):
        url = reverse('usersAPI:api_send_new_password')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure user's password is updated in the database
        self.user1.refresh_from_db()
        self.assertNotEqual(self.user1.check_password('testpassword'), True)

        # Add more assertions as needed
