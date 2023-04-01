from django.urls import path
from .views import (
    api_home,
    BooksCategoryList,
    BooksCategoryDetail,
    BooksList,
    BooksDetail,
    FeaturedBooksList,
    FeaturedBooksDetail,
    )

urlpatterns = [
    # path('', api_home, name='home'),
    path('books/', BooksList.as_view(), name='books'),
    path('books/<int:pk>', BooksDetail.as_view(), name='books-detail'),
    path('featured-books/', FeaturedBooksList.as_view(), name='featured-books'),
    path('featured-books/<int:pk>', FeaturedBooksDetail.as_view(), name='featured-books-detail'),
    path('books-category/', BooksCategoryList.as_view(), name='books-category'),
    path('books-category/<int:pk>', BooksCategoryDetail.as_view(), name='books-category-detail'),
]