from pyexpat import model
from rest_framework import serializers
from .models import Books, BooksCategory, FeaturedBooks


class BooksCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksCategory
        fields = (
            'id',
            'name',
            'image',
            'alt',
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = (
            'id',
            'title',
            'author',
            'cover_image',
            'alt',
            'book_url',
            'category',
        )


class FeaturedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedBooks
        fields = (
            'id',
            'title',
            'author',
            'cover_image',
            'alt',
            'book_url',
        )