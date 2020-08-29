from datetime import datetime
import json

from django.core.management.base import BaseCommand

from rates.models import ECBRate


class Command(BaseCommand):
    help = "bulk load some rates into the database from a JSON file"
    DEFAULT_FILE_PATH = "data/ecb_rates_initial.json"

    def print_count(self, cls_name, count):
        print(f"{cls_name} has {count} elements")

    def handle(self, *args, **options):
        self.print_count(ECBRate.__name__, ECBRate.objects.all().count())
        with open(self.DEFAULT_FILE_PATH) as file:
            data = json.load(file)
        # TODO: this is a serialization problem which is currently "hacked"
        for n, elm in enumerate(data):
            data[n]["dt"] = datetime.strptime(elm["dt"], "%Y-%m-%d").date()
        ECBRate.objects.bulk_create([ECBRate(**elm) for elm in data])
        self.print_count(ECBRate.__name__, ECBRate.objects.all().count())
