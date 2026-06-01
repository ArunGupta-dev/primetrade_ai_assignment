from django.urls import path
from authentication.views import*
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
        path('auto_auth/', auto_auth),
        path('signup/', signup),
        path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

