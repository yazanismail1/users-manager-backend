from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SignInView, SignUpView

urlpatterns = [
    path('signin/', SignInView.as_view()),
    path('signup/', SignUpView.as_view()),

]
