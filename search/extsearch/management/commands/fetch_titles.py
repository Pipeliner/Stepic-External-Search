from django.core.management.base import BaseCommand, CommandError
import json
import requests

class Command(BaseCommand):
    help = 'Fetches Stepic lessons titles (via API) to local database'

    def handle(self, *args, **options):
        page = 1
        while True:
            answer = requests.get("https://stepic.org/api/lessons", params={'page': 1})
            if answer.status_code == 404:
                break

            self.stdout.write(str(answer.json()['meta']['has_next']))

            page += 1
