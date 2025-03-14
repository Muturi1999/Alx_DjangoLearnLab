# # from django.contrib import admin
# # from .models import Book  


# # @admin.register(Book)
# # class BookAdmin(admin.ModelAdmin):
# #     list_display = ('title', 'author', 'publication_year') 
# #     search_fields = ('title', 'author')  
# #     list_filter = ('publication_year',) 
# from django.contrib import admin
# from .models import Book, CustomUser

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'publication_year')
#     search_fields = ('title', 'author')
#     list_filter = ('publication_year',)

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'date_of_birth', 'is_staff')
#     search_fields = ('username', 'email')
#     list_filter = ('is_staff', 'is_superuser')

# admin.site.register(Book, BookAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from .models import Book, CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser')
