from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
# Create your models here.
class ArticleSeries(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False, blank=False, default='')
    published = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']
    def __str__(self):
        return self.title
class Article(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=100, default='', blank=True)
    article_slug = models.SlugField(unique=True, null=False, blank=False, default='')
    content = HTMLField(blank=True, default='')
    notes = HTMLField(blank=True, default='')
    published = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    series = models.ForeignKey(ArticleSeries, on_delete=models.SET_DEFAULT, default="", verbose_name="Series")
    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']
    def __str__(self):
        return self.title
    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

