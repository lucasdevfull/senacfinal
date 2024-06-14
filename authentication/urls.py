from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.RegisterView.as_view(), name='cadastro'),
    path('',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout')
]