from django.contrib import admin
from notice.models import Notice, Comment
from re import search

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['notice', 'content', 'pubDateTime']
#    list_display_links = ['notice']
    list_filter = ['notice', 'content']
    search_fields = ['content']
    list_editable = ['content']
    
    class Meta:
        model = Comment


admin.site.register(Notice)
admin.site.register(Comment, CommentAdmin)