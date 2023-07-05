from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("bible/<int:testament>/<int:bookno>/<int:chapter>/",views.show_bible_content,name="show_bible_content"),
    path("bible/ajax/<int:testament>/<int:bookno>/<int:chapter>/",views.show_content_ajax_call,name="show_content_ajax_call"),
]



    
