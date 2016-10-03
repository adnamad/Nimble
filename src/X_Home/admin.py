from django.contrib import admin
from .models import Articles,contact

# Register your models here.


admin.site.register(Articles)
admin.site.register(contact)




# from django.contrib import admin
# from .models import Author
# from guardian.admin import GuardedModelAdmin

# # Old way:
# #class AuthorAdmin(admin.ModelAdmin):
# #    pass

# # With object permissions support
# class AuthorAdmin(GuardedModelAdmin):
#     pass

# admin.site.register(Author, AuthorAdmin)