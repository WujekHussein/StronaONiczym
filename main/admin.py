from django.contrib import admin
from .models import Article, ArticleSeries

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Header' , {"fields" : ['title', 'subtitle', 'slug', 'series']}),
        ('Content', {"fields" : ['content', 'notes']}),
        ('Date',  {"fields" : ['modified']}),
    ]

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        'published'
    ]


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
