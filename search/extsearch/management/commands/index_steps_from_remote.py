from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
import requests

class Command(BaseCommand):
    help = 'Fetches Stepic steps titles (via API) to local Elasticsearch'

    def handle(self, *args, **options):
        es = Elasticsearch()

        page = 1
        while True:
            answer = requests.get("https://stepic.org/api/steps", params={'page': page})
            if answer.status_code == 404:
                break

            #print(answer.json())

            steps = answer.json()['steps']
            for step in steps:
                step_body = {
                    'id': step['id'],
                    'lesson': step['lesson'],
                    'text': step['block']['text']
                }
                es.index(index='stepic-steps', doc_type='steps', id=step['id'], body=step_body)

            if page % 1 == 0:
                self.stdout.write('Saved steps from page %s' % page)

            page += 1
