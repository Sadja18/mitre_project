from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

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

def determine_likely_groups(input):
    # Deserialize the JSON input and extract tactic IDs, techniques, and sub-techniques
    tactics = []
    techniques = []
    sub_techniques = []

    for item in json_input:
        tactic_id = item.get('tactic_id')
        techniques.extend(item.get('techniques', {}).keys())
        sub_techniques.extend(sub_tech for technique in item.get('techniques', {}).values() for sub_tech in technique)

        tactics.append(tactic_id)

    # Iterate through adversary groups and calculate matching score
    group_scores = {}

    for group in AdversaryGroup.objects.all():
        score = 0

        for tactic in group.preferred_techniques.all():
            if tactic.id in tactics:
                score += 1

                technique_ids = techniques
                if tactic.id in technique_ids:
                    score += 1

                    sub_technique_ids = sub_techniques
                    if tactic.id in sub_technique_ids:
                        score += 1

        group_scores[group.group_name] = score

    # Sort the groups based on matching score
    sorted_groups = sorted(group_scores.items(), key=lambda x: x[1], reverse=True)

    return sorted_groups

class LikelyAdversaryGroupsView(APIView):
    def post(self, request, format=None):
        json_input = request.data

        likely_groups = determine_likely_groups(json_input)

        return Response(likely_groups)