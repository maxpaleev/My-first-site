from django.urls import path
from . import views

urlpatterns = [
    path("", views.work_home, name="work_home"),
    path('create', views.work_create, name='work-create'),
    path('<int:pk>', views.WorkDetail.as_view(), name='Detail'),
    path('<int:pk>/update', views.WorkUpdate.as_view(), name="WorkUpdate"),
    path('<int:pk>/delete', views.WorkDelete.as_view(), name="WorkDelete")

]
