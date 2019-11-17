from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
      path('<int:question_id>/', detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', results, name='results'),
    # ex: /polls/5/vote/
    path('vote/<int:id>', vote, name='vote'),
]
