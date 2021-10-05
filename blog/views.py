import json
from datetime import timedelta, datetime
from django.http import JsonResponse, response
from django.views import View
# from elasticsearch import Elasticsearch

from .models import Booklist
# # from .documents import BookDocument


class Book(View):
    def get(self, request):
        search_data = request.GET['search']
        data = Booklist.objects.all()
        data = {
            'name' : data.name,
            'category' : data.category,
            'tag' : data.tag
        }
        JsonResponse({'message' : data}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        
        Booklist.objects.create(
            name = data['name'],
            category = data['category']
        )

        return JsonResponse({'message' : 'success'}, status=200)