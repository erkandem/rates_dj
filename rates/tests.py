import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode
from parameterized import parameterized
import pytest
from rest_framework import status

from utilities import to_camel_case

from .factorys import ECBRateFactory
from .serializers import (
    ECBRateSerializer,
    ECBRateSerializerDetails,
)


@pytest.mark.integration_test
class TestECBRate(TestCase):
    def setUp(self):
        self.date_strings = [
            "2019-01-01",
            "2019-01-02",
            "2019-01-03",
            "2019-01-04",
        ]
        self.dates = [
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            for date_str in self.date_strings
        ]
        for date_ in self.dates:
            ECBRateFactory(dt=date_)

    def test_complete_curve(self):
        """
        TODO: learn to use reverse with API to get the URL of a resource
        """
        response = self.client.get(
            reverse("api-ecbrates")
        )
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_data["results"], list)
        self.assertTrue(len(response_data["results"]) > 0)
        self.assertEqual(
            set(response_data["results"][0].keys()),
            set(ECBRateSerializer.Meta.fields)
        )

    @parameterized.expand(
        ECBRateSerializerDetails.ECB_RATE_SERIALIZER_VALUE_FIELDS
    )
    def test_single_column(self, rate_param):
        uri = reverse(
            "api-ecbrates-single",
            kwargs={"rate_duration": rate_param, }
        )
        response = self.client.get(uri)
        response_data = response.data
        self.assertIsInstance(response_data["results"], list)
        self.assertTrue(len(response_data["results"]) > 0)
        self.assertEqual(
            set(response_data["results"][0].keys()),
            {
                *ECBRateSerializerDetails.ECB_RATE_SERIALIZER_PK_FIELDS,
                rate_param
            }
        )

    @parameterized.expand([
        (reverse("api-ecbrates"),),
        (reverse(
            "api-ecbrates-single",
            kwargs={
                "rate_duration": ECBRateSerializerDetails.ECB_RATE_SERIALIZER_VALUE_FIELDS[0],
            }
        ),),
    ])
    def test_complete_curve_with_filtering(self, uri):
        start_date_keyword = "start_date"
        end_date_keyword = "end_date"

        earlier_than_start_date = self.date_strings[1]
        start_date_string = self.date_strings[2]
        end_date_string = self.date_strings[3]

        query_params = {
            to_camel_case(start_date_keyword): start_date_string,
            to_camel_case(end_date_keyword): end_date_string,
        }
        response = self.client.get(
            uri
            + "?"
            + urlencode(query_params),
        )
        response_data = response.data
        date_strings_in_response = [row["dt"] for row in response_data["results"]]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn(earlier_than_start_date, date_strings_in_response)
        self.assertIn(start_date_string, date_strings_in_response)
        self.assertIn(end_date_string, date_strings_in_response)
