from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    query_string = request.GET['q'] if 'q' in request.GET else ""
    return render(request, 'extsearch/index.html', {'query_string': query_string, 'search_results': "Fake search results"})
