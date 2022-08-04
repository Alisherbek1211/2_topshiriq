from django.urls import path
from chat import views
urlpatterns = [
    path("chat/",views.ChatListView.as_view()),
    path('message/<int:pk>/',views.MessageListView.as_view()),
    path('message/<int:pk>/update/',views.MessageUpdateView.as_view()),
    path('message/<int:pk>/delete/',views.MessageDeleteView.as_view()),

]