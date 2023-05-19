from django.http import JsonResponse
from .models import Tactic

def search_tactics(request):
    query = request.GET.get('query')
    tactics = Tactic.objects.filter(tactic_name__icontains=query)
    results = [{'id': tactic.id, 'name': tactic.tactic_name} for tactic in tactics]
    return JsonResponse(results, safe=False)
