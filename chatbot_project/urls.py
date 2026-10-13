from django.urls import path
from chatbot.views import home,chat
urlpatterns=[path("",home,name="home"),path("chat/",chat,name="chat")]
