from django.core.management.base import BaseCommand, CommandError
import requests

from extsearch.models import Lesson

class Command(BaseCommand):
    help = 'Fetches Stepic lessons titles (via API) to local database'

    def handle(self, *args, **options):
        page = 1
        while True:
            answer = requests.get("https://stepic.org/api/lessons", params={'page': page})
            if answer.status_code == 404:
                break

            lessons = answer.json()['lessons']
            for lesson in lessons:
                local_lesson = Lesson(id=lesson['id'], title=lesson['title'])
                local_lesson.save()

            if page % 10 == 0:
                self.stdout.write('Saved lessons from page %s' % page)

            page += 1
