from django.contrib import admin
from newhome.models import Book,Author,Genre,Student

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
#jadmin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=('id','name')
    fields=[('name','purchase_date'),('genre','book_author')]
    list_filter=('name','purchase_date',('book_author',admin.RelatedOnlyFieldListFilter))

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields=('id','author_name')
    list_filter=('author_name','timestamp')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('student_id','student_name')
    #list_filter=('author_name','timestamp')

