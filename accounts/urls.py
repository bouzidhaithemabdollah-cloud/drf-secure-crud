from django.urls import path 
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/",view=views.register_user,name="register"),
    path("users/<uuid:id>/",view=views.get_user,name="getting"),
    path("users/<uuid:id>/delete/",view=views.delete_user,name="deleting"),
    path("users/<uuid:id>/update/",view=views.update_user,name='update'),
    path("api/token/",view=TokenObtainPairView.as_view(),name="access token obtian pair"),
    path("api/refresh/",view=TokenRefreshView.as_view(),name="refresh token")


]
