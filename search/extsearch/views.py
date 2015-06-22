from django.shortcuts import render
from elasticsearch import Elasticsearch

def index(request):
    query_string = request.GET['q'] if 'q' in request.GET else ""
    es = Elasticsearch()
    elastic_results = es.search(index="stepic", body={"query": {"match": { "title": query_string}}})
    hits = elastic_results['hits']['hits']
    response_results = [{'id': hit['_id'], 'title': hit['_source']['title']} for hit in hits]
    query_results = {'query_string': query_string, 'search_results': response_results}
    return render(request, 'extsearch/index.html', query_results)
