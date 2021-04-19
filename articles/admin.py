from django.contrib import admin 
from .models import Article, Comment

# below 2x class for tabularInline comments in admin panel

class CommentInline(admin.TabularInline): 
    model = Comment

class ArticleAdmin(admin.ModelAdmin): 
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
