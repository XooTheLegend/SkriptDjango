from django.urls import path, re_path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.index, name='vesti'),
    path('korisnici/',views.korisnici, name='korisnici'),
    path('komentari/',views.komentari,name='komentari'),
    path('int/<br>', views.broj, name='vesti_broj'),
    path('params/', views.query, name='vesti_query'),
    re_path(r'^regex/(?:godina-(?P<godina>[0-9]{4}))/(?:mesec-(?P<mesec>[0-9]{2}))', views.regex, name='vesti_regex'),#re_path = regex path
]