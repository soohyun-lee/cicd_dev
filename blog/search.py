# from elasticsearch_dsl.connections import connections
# from elasticsearch_dsl import Text, Date, Integer, Document, Search
# from elasticsearch.helpers import bulk
# from elasticsearch import Elasticsearch

# from . import models

# connections.create_connection()

# class BookListIndex(Document):
#     id = Integer()
#     name = Text()
#     category = Text()

#     class Index:
#         name = 'booklist-index'
    
# def bulk_indexing():
#     BookListIndex.init()
#     es = Elasticsearch()
#     bulk(clinet=es, actions=(b.indexiing() for b in models.BookList.objects.all().iterator()))

# def search(category):
#     s = Search().filter('match', category=category)
#     response = s.execute()
#     return response
    
