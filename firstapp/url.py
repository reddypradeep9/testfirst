
from django.urls import path
from firstapp import views

urlpatterns = [
    path('nextikkada/',views.studentview,name="studentview"),
    path('thank/',views.thankview,name="thankview"),

]
