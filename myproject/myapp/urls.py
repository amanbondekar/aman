from django.urls import path
from .views import CustomLoginView, SignUpView

app_name = 'myapp'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLoginView.as_view(), name='logout'),

    path('signup/', SignUpView.as_view(), name='signup'),

]
