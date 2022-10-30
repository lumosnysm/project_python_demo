from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'tinhtuoi'

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.calculate, name='calculate'),
    path('feedback/', views.feedback, name='feedback'),
    path('gen_doc/', views.gen_doc, name='gen_doc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
