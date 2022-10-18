from django.test import TestCase
from django.test import Client
from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from django.test import Client


class URLTests(TestCase):
    def test_testhomepage(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', password='test_user')
        self.client.login(username='testuser', password='test_user')

        response = self.client.get("/chat/")
        self.assertEqual(response.status_code, 200)
