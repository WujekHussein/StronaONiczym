from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path("<series>", views.series, name="series"),
    path("<series>/<article>", views.article, name="article")
]