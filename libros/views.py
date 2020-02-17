from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import FormView, UpdateView
from django.http import JsonResponse
from libros.models import Author, Book
from libros.forms import BookForm


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
