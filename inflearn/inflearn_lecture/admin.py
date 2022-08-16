from django.contrib import admin
from .models import myText, Comment

class MyTextAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


admin.site.register(myText, MyTextAdmin)
admin.site.register(Comment)

# Register your models here.
