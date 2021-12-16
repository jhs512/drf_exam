from django.contrib import admin

# Register your models here.
from article_api.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "create_date", "author", "title"]
    search_fields = ["title"]

    class Meta:
        model = Article

admin.site.register(Article, ArticleAdmin)