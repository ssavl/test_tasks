from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('poll/', views.PollList.as_view()),
    path('pool/<int:pk>', views.PollDetail.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>', views.QuestionDetail.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('answers/<int:pk>', views.AnswerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
