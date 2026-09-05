from django.urls import path 
from . import views

urlpatterns = [
    path("register/",view=views.register_user,name="register"),
    path("users/<uuid:id>/",view=views.get_user,name="getting"),
    path("users/<uuid:id>/delete/",view=views.delete_user,name="deleting"),
    path("users/<uuid:id>/update/",view=views.update_user,name='update')


]
