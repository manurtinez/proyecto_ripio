"""ripio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework import routers, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from monedas import views
from monedas.views import validate_token

# Generar rutas para las vistas
router = routers.DefaultRouter()
router.register(r'monedas', views.MonedaViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'balances', views.MonedaUsuarioViewSet)

# Schema view para swagger
schema_view = swagger_get_schema_view(
    openapi.Info(
        title="API docs",
        default_version='1.0.0',
        description="API docs",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', views.LoginView.as_view()),
    # path('logout/', views.LogoutView.as_view()),
    path('transferencias/', views.TransferenciaViewSet.as_view({'get': 'list'})),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/validate/', validate_token, name='token_verify'),
]
