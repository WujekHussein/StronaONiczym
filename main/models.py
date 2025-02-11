from django.db import models
from django.utils import timezone
# Create your models here.
class ArticleSeries(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False, blank=False)
    published = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']
class Article(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=100, default='', blank=True)
    slug = models.SlugField(unique=True, null=False, blank=False)
    content = models.TextField()
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
        return self.slug

