from django.test import TestCase
import pytest
from rest_framework import status

from .factorys import ECBRateFactory
from .serializers import ECBRateSerializer


@pytest.mark.integration_test
class TestECBRate(TestCase):
    def test_basic(self):
        """
        Not really a test which makes a lot of sense.
        It's the first. You know, to have one.
        Todo: learn to use reverse with API router to get the URL of a ressource
        from django.urls import reverse
        """
        ECBRateFactory()
        response = self.client.get("/api/v1/rates/ecb/")
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_data, list)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(
            set(response_data[0].keys()), set(ECBRateSerializer.Meta.fields)
        )
