from django.contrib import admin

from .models import Student,Book,BookRecord,Author

admin.site.register([Student,Book,BookRecord])
admin.site.register(Author)




