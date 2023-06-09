from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, signup


urlpatterns = [
    path("me", home, name='home'),
    path("signup", signup, name="signup"),
    path("login", LoginView.as_view(template_name='registration/login.html', next_page='home'), name="login"),
    path("logout", LogoutView.as_view(next_page='home'), name="logout"),
]
