from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from sub_techniques.models import SubTechnique

def get_subtechniques(request):

    print('get subtech')
    technique_id = request.GET.get('technique_id')
    print(technique_id)
    sub_techniques = SubTechnique.objects.filter(technique_id=technique_id).values('id', 'name')
    print(sub_techniques)
    return JsonResponse({'sub_techniques': list(sub_techniques)})