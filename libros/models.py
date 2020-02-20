from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "{0} {1}".format(self.name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey('author', on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=13, null=False, blank=False)
    editorial = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return "{0} - {1}".format(self.title, self.author)
