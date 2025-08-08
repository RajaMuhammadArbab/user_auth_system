from django.urls import path
from .views import RegisterView, UserListView, UserDeleteView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
  
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:user_id>/', UserDeleteView.as_view(), name='user_delete'),

    path('profile/', ProfileView.as_view(), name='profile'),
]
