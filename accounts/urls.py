from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginView, SignUpView

urlpatterns = [
    path('', LoginView.as_view()),
    path('signup/', SignUpView.as_view()),

]
