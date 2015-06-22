from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch

from extsearch.models import Lesson

class Command(BaseCommand):
    help = 'Fetches Stepic lessons titles (via API) to local database'

    def handle(self, *args, **options):
        lessons = Lesson.objects.all()
        self.stdout.write('Indexing %s lessons' % len(lessons))
        es = Elasticsearch()
        for lesson in lessons:
            lesson_body = {'title': lesson.title}
            es.index(index='stepic', doc_type='lessons', id=lesson.id, body=lesson_body)

        self.stdout.write('Done.')
