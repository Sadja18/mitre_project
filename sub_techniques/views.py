from django.http import JsonResponse
from django.shortcuts import render

from techniques.models import Technique

# Create your views here.
def search_techniques(request):
    query = request.GET.get('query')
    techniques = Technique.objects.filter(tactic_name__icontains=query)
    results = [{'id': technique.id, 'name': technique.technique_name} for technique in techniques]
    return JsonResponse(results, safe=False)