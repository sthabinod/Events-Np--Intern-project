from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    link = models.URLField()

    def __str__(self):
        return self.full_name

class Organiser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField()
    description = models.CharField(max_length=255)
    featured = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)
    date_edited = models.DateField()

    def __str__(self):
        return self.name

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_static/images/event_images')
    link = models.URLField()


    def __str__(self):
        return self.name


class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    time = models.DateTimeField()
    speaker = models.ForeignKey(Speaker, models.DO_NOTHING)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    program = models.ManyToManyField(Program)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    featured_image = models.ImageField(null=True,upload_to='event_static/images/event_images')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    tags = models.CharField(max_length=100)
    organiser = models.ForeignKey(Organiser, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    date_added = models.DateField(auto_now_add=True)
    date_edited = models.DateField()
    featured = models.BooleanField()
    block = models.BooleanField()
    schedule = models.ManyToManyField(Schedule)

    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField(upload_to='files')
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.file
