from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from libros.models import Author, Book


# class AuthorSerilizer2(Serializer):
#     first_name = serializers.CharField(required=True, source='name')
#     last_name = serializers.CharField(required=True)


def startsWithA(value):
    if value[0].capitalize() != 'A':
        raise serializers.ValidationError('This field must start with A|a.')


class BookSerializer(ModelSerializer):
    # author = AuthorSerilizer()
    # author = serializers.StringRelatedField()
    # author = serializers.HyperlinkedRelatedField(
    #     view_name='api author', queryset=Author.objects.all()
    # )

    class Meta:
        model = Book
        exclude = ()


class AuthorSerilizer(ModelSerializer):
    first_name = serializers.CharField(
        required=True, source='name', validators=(startsWithA,)
    )
    last_name = serializers.CharField(
        required=True, source='name', validators=(startsWithA,)
    )

    books = BookSerializer(
        many=True, read_only=True, source='book_set'
    )

    class Meta:
        model = Author
        exclude = ('name',)
