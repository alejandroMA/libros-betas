from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import FormView, UpdateView
from django.http import JsonResponse
from libros.models import Author, Book
from libros.forms import BookForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
# from rest_framework.exceptions import APIException, ValidationError
from rest_framework.permissions import IsAuthenticated
from libros.serializers import AuthorSerilizer, BookSerializer


class ListAuthorApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerilizer(authors, many=True)

        # raise Exception('error')
        # raise ValidationError('hiciste algo mal')

        return Response(serializer.data)


class AuthorApi(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerilizer


class BookApi(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRegister(FormView):
    template_name = "bookForm.html"
    form_class = BookForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


class BookEdit(UpdateView):
    template_name = "bookForm.html"
    form_class = BookForm
    model = Book
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


class BooksList(View):
    def get(self, request):
        authors = Author.objects.all()

        # raise Exception(authors[0].book_set.all())

        contex = {
            'authors': authors
        }

        return render(request, "bookList.html", context=contex)

    def post(self, request):
        return render(request, "bookList.html", context={'authors': []})


class BookDelete(View):
    def post(self, request):
        book = get_object_or_404(Book, id=request.POST['id'])
        book.delete()

        return JsonResponse({'success': True})
