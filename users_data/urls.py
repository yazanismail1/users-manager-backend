from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ContentView, UpdateView, CreateView, CertainDataView, DeleteView

urlpatterns = [
    path('', ContentView.as_view(), name='home'),
    path('certainData/<int:pk>', CertainDataView.as_view()),
    path('create/', CreateView.as_view()),
    path('update/<int:pk>', UpdateView.as_view()),
    path('delete/<int:pk>', DeleteView.as_view())
]