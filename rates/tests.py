from datetime import date

from django.test import TestCase
import pytest
from rest_framework import status

from .factorys import ECBRateFactory
from .serializers import (
    ECBRateSerializer,
    ECBRateSerializerDetails,
)


@pytest.mark.integration_test
class TestECBRate(TestCase):
    def setUp(self):
        ECBRateFactory(dt=date(2019, 1, 1))
        ECBRateFactory(dt=date(2019, 1, 2))

    def test_complete_curve(self):
        """
        Not really a test which makes a lot of sense.
        It's the first. You know, to have one.
        TODO: learn to use reverse with API to get the URL of a resource
        from django.urls import reverse
        """
        response = self.client.get("/api/v1/rates/ecb/")
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_data['results'], list)
        self.assertTrue(len(response_data['results']) > 0)
        self.assertEqual(
            set(response_data['results'][0].keys()),
            set(ECBRateSerializer.Meta.fields)
        )

    def test_single_column(self):
        """
        TODO: learn to use reverse with API to get the URL of a resource
        """
        rate_param = ECBRateSerializerDetails.ECB_RATE_SERIALIZER_VALUE_FIELDS[0]
        response = self.client.get("/api/v1/rates/ecb/%s/" % rate_param)
        response_data = response.data
        self.assertIsInstance(response_data['results'], list)
        self.assertTrue(len(response_data['results']) > 0)
        self.assertEqual(
            set(response_data['results'][0].keys()),
            {
                *ECBRateSerializerDetails.ECB_RATE_SERIALIZER_PK_FIELDS,
                rate_param
            }
        )
