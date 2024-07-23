from django.urls import path
from .views import home, signup, user_login, user_logout, profile


urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name='login'),
    
]
