from django.core.management.base import BaseCommand, CommandError
import requests

from extsearch.models import Step

class Command(BaseCommand):
    help = 'Fetches Stepic steps texts (via API) to local database'

    def handle(self, *args, **options):
        page = 1
        while True:
            answer = requests.get("https://stepic.org/api/steps", params={'page': page})
            if answer.status_code == 404:
                break

            steps = answer.json()['steps']
            for step in steps:
                local_step = Step(id=step['id'], text=step['block']['text'], lesson_id=step['lesson'])
                local_step.save()

            if page % 10 == 0:
                self.stdout.write('Saved steps from page %s' % page)

            page += 1
