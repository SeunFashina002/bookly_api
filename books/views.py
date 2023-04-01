from django.shortcuts import render
from django.db.models import Q
from .serializers import BookSerializer, FeaturedBookSerializer, BooksCategorySerializer
from .models import Books, BooksCategory, FeaturedBooks
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])

def api_home(request):    
    data="Welcome to bookly api, kindly visit the api documentation to use. Happy usage :)"
    return Response(data)

class BooksCategoryList(ListCreateAPIView):
    queryset = BooksCategory.objects.all()
    serializer_class = BooksCategorySerializer

class BooksCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = BooksCategory.objects.all()
    serializer_class = BooksCategorySerializer



class BooksList(ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BooksDetail(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer



class FeaturedBooksList(ListCreateAPIView):
    queryset = FeaturedBooks.objects.all()
    serializer_class = FeaturedBookSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        qs = FeaturedBooks.objects.all()
        if search is not None:
            qs = FeaturedBooks.objects.filter(
                Q(title__icontains=search) | Q(author__icontains=search)
            )
        return qs

class FeaturedBooksDetail(RetrieveUpdateDestroyAPIView):
    queryset = FeaturedBooks.objects.all()
    serializer_class = FeaturedBookSerializer


