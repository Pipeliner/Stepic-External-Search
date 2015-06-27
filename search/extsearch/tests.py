from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Lesson

class LessonSearchTests(TestCase):
    def test_index_view_with_no_search_results(self):
        request_string = "ThereIsNoLessonWithThisTitle"
        response = self.client.get(reverse('index'), {'q': request_string})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, request_string)
        self.assertEqual(response.context['search_results'], [])

    def test_index_view_with_one_search_result(self):
        request_string = "clojure"
        # Django uses fresh db for tests by default
        # so we either have to make it reuse db
        # or just recreate it manually
        lesson = Lesson(id=11181, title='Clojure Test')
        lesson.save()
        response = self.client.get(reverse('index'), {'q': request_string})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, request_string)
        self.assertEqual(response.context['search_results'], [Lesson.objects.get(title='Clojure Test')])

