from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CustomUserViewSet, LoginView, LogoutView

router = SimpleRouter()

router.register(r'custom_user', CustomUserViewSet)

urlpatterns = router.urls + [
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),
]