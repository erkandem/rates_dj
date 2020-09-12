import typing

from rest_framework.exceptions import NotFound
from rest_framework.serializers import ModelSerializer

from .models import ECBRate


class ECBRateSerializerDetails:
    ECB_RATE_SERIALIZER_PK_FIELDS = [
        "dt",
    ]
    ECB_RATE_SERIALIZER_VALUE_FIELDS = [
        "rate_3m",
        "rate_4m",
        "rate_6m",
        "rate_9m",
        "rate_1y",
        "rate_2y",
        "rate_5y",
        "rate_7y",
        "rate_10y",
        "rate_15y",
        "rate_30y",
    ]
    ECB_RATE_SERIALIZER_FIELDS = [
        *ECB_RATE_SERIALIZER_PK_FIELDS,
        *ECB_RATE_SERIALIZER_VALUE_FIELDS,
    ]


class ECBRateSerializerFieldNameValidation:
    @staticmethod
    def validate_path_param(
            path_param: str
    ) -> typing.Union[str, None]:
        """
        Validate that a path param is on the allowlist.
        The caller decides on how to react.

        Args:
            path_param (str):

        Returns:
            str returns the input if ``path_param`` is valid
            None if if input is invalid
        """
        if path_param in ECBRateSerializer.Meta.fields:
            return path_param
        else:
            return None


class ECBRateSerializer(
    ECBRateSerializerFieldNameValidation,
    ModelSerializer,
):

    class Meta:
        model = ECBRate
        fields: typing.List[str] = ECBRateSerializerDetails.ECB_RATE_SERIALIZER_FIELDS

    def __init__(
            self,
            *args: typing.Any,
            **kwargs: typing.Any
    ):
        """
        Hack to have dynamic set of serialized fields.
        if the keyword behind ``rate_duration``, which is part of the URL
        is present it will limit the serialized field only to
        the rate which is specifically tried to access
        + the primary key (``always_included``)

        Args:
            *args:
            **kwargs:
        """
        super().__init__(*args, **kwargs)
        if 'context' in kwargs:
            if 'view' in kwargs['context']:
                if 'rate_duration' in kwargs['context']['view'].kwargs:
                    rate_duration = kwargs['context']['view'].kwargs['rate_duration']
                    rate_duration = self.validate_path_param(rate_duration)
                    if rate_duration:
                        allowed = {
                            rate_duration,
                            *ECBRateSerializerDetails.ECB_RATE_SERIALIZER_PK_FIELDS
                        }
                        available = set(self.fields.keys())
                        for field_name in available - allowed:
                            self.fields.pop(field_name)
                    else:
                        raise NotFound(detail=(
                                f'Received `{rate_duration}`. '
                                'Defined paths are: `'
                                + '`, '.join(
                                    ECBRateSerializerDetails.ECB_RATE_SERIALIZER_VALUE_FIELDS
                                )
                                + '`'
                        ))
