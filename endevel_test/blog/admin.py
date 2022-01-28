from django.contrib import admin
from blog.models import Article, Tag


class TagAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
