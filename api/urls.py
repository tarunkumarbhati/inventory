from django.urls import path
from .views import BoxView, MyBoxView


urlpatterns = [
    path('boxes/<int:pk>', BoxView.as_view()),
    path('boxes/', BoxView.as_view()),
    path('my-boxes/', MyBoxView.as_view()),
]