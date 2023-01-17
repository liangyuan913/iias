from django.contrib import admin
from notice.models import Notice, Comment

# Register your models here.

admin.site.register(Notice)
admin.site.register(Comment)