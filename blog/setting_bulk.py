# from elasticsearch import Elasticsearch

# es = Elasticsearch()

# es.indices.create(
#     index='dictionary',
#     body={
#         "settings": {
#             "index": {
#                 "analysis": {
#                     "analyzer": {
#                         "my_analyzer": {
#                             "type": "custom",
#                             "tokenizer": "nori_tokenizer"
#                         }
#                     }
#                 }
#             }
#         },
#         "mappings": {
#             "properties": {
#                 'id' : {
#                     "type" : "long"
#                 },
#                 "name": {
#                     "type": "text",
#                     "analyzer": "my_analyzer"
#                 },
#                 "category": {
#                     "type": "text",
#                     "analyzer": "my_analyzer"
#                 }
#             }
#         }
#     }
# )