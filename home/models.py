from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.PositiveSmallIntegerField(default=18,blank=True,null=True)
    p_num = models.CharField(max_length =12,null=True,blank=True)
    email = models.EmailField()
    gender = models.CharField(max_length=6,blank=True,null=True)
    city = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    GENDER_F =(
        ('male',"Male"),
        ('female','Female'),
    )

    name = models.CharField(max_length= 100)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=6,choices=GENDER_F)
    city = models.CharField(max_length=30)
    is_alive = models.BooleanField(default=True)
    img = models.FileField(upload_to=f'image/author')
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=60)
    yil = models.IntegerField()
    genre = models.CharField(max_length=50)
    page = models.PositiveIntegerField()
    # author = models.ManyToManyField(Author)
    is_active = models.BooleanField()

    def __str__(self):
        return self.title

class BookAuthor(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.book} by {self.author} "




class BookRecord(models.Model):
    book = models.ForeignKey(Book, models.CASCADE)
    student = models.ForeignKey(Student, models.CASCADE)
    date = models.IntegerField(default=1)


    def __str__(self):
        return f"{ self.student.name} take {self.book.name}"

    def __repr__(self):
        return "salom"

print("salom ")
