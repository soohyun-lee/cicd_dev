from django.urls import path, include



urlpatterns = [
    path('book', include('blog.urls')),
]
