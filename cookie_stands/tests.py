from django.test import TestCase
from .models import CookieStand
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class TestCookie(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user=get_user_model().objects.create(username='user1',password='password')
        cls.user.save()

        cls.cookie=CookieStand.objects.create(location='location', owner=cls.user ,description='description',
                                 hourly_sales=None,minimum_customers_per_hour=13,maximum_customers_per_hour=42,
                                 average_cookies_per_sale=3.6)
        cls.cookie.save()

    def setUp(self) -> None:
        self.client.login(username='user1', password='password')

    def test_get_cookie_list(self):
        url=reverse("cookie_stand_list")
        response=self.client.get(url)
        self.assertEqual(response.status_code , status.HTTP_200_OK)

