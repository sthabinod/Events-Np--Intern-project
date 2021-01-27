from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
