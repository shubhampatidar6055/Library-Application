from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return (self.name)

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return (self.book_name)

class Issuebook(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, default=True)


    def __str__(self):
        return (self.name)
