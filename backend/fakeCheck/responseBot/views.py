from django.http import JsonResponse
from django.shortcuts import redirect

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

class CompareQuery(APIView):
    parser_classes = [JSONParser]

    def post(self, request, format=None):

        query1 = request.data['inputQuery1']
        query2 = request.data['inputQuery2']

        return Response({
            "inputQuery1": query1,
            "inputQuery2": query2,
            "comparisonMetrics": {
                "SemanticSimilarity": 30.0,
                "DoTheyAgree": True,
                "otherKindOfSimilarity": 32.0,
            }
        })
    
    def get(self, request):
        return redirect("https://hrs2203.github.io/fuzzy-pancake/frontend/queryComparision.html")
