import json
from django.http import JsonResponse
from django.views import View
from .models import Booklist

class Book(View):
    def get(self, request):
        all_booklist = Booklist.objects.all()

        data = ['aws', 'test']
        a = Booklist.objects.filter(name__in=data)
        if a.count() == len(data):
            return JsonResponse({'message' : data}, status=200) 
        else:
            return JsonResponse({'message' : 'no'}, status=200) 

        data = [{
            'name' : book.name,
            'category' : book.category
        } for book in all_booklist]

        return JsonResponse({'message' : data}, status=200)

# @api.get('/items/1')
# def get(request, item_id: int):
#     return {"date" : item_id}
#     all_booklist = Booklist.objects.all()

#     data = [{
#         'name' : book.name,
#         'category' : book.category
#     } for book in all_booklist]

#     return JsonResponse({'message' : data}, status=200)