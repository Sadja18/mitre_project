from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from django.http import JsonResponse
from adversary_techniques.models import AdversaryTechniques
from sub_techniques.models import SubTechnique
from tactics.models import Tactic
from techniques.models import Technique

def get_subtechniques(request):

    print('get subtech')
    technique_id = request.GET.get('technique_id')
    print(technique_id)
    sub_techniques = SubTechnique.objects.filter(technique_id=technique_id).values('id', 'name')
    print(sub_techniques)
    return JsonResponse({'sub_techniques': list(sub_techniques)})

def determine_likely_groups(json_list):
    # Deserialize the JSON input and extract tactic IDs, techniques, and sub-techniques
    try:
        matches = {}

        for item in json_list:
            tactic_id = item['tactic_id']
            techniques = item['techniques']
            tactic = Tactic.objects.get(tactic_id=tactic_id)
            
            for technique in techniques:
                technique_id = technique['technique_id']
                subtechnique_ids = technique['sub-techniques']
                technique = Technique.objects.get(technique_id=technique_id)
                
                if subtechnique_ids:
                    subtechniques = SubTechnique.objects.filter(id__in=subtechnique_ids)
                    adversary_techniques = AdversaryTechniques.objects.filter(tactic=tactic, technique=technique, sub_technique__in=subtechniques)
                else:
                    adversary_techniques = AdversaryTechniques.objects.filter(tactic=tactic, technique=technique)
                
                for adversary_technique in adversary_techniques:
                    adversary_group = adversary_technique.adversary_group
                    
                    if adversary_group in matches:
                        matches[adversary_group] += 1
                    else:
                        matches[adversary_group] = 1

    except Exception as e:
        print('error occurred' )
        print(e)
        return None

class LikelyAdversaryGroupsView(APIView):
    def post(self, request, format=None):
        json_input = request.data

        likely_groups = determine_likely_groups(json_input)

        return Response({
            "record":likely_groups
            })