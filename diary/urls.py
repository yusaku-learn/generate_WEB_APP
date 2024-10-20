from django.urls import path
from . import views

app_name = "diary"
urlpatterns = [
    path("",views.index,name="index"),
    path('success_page/', views.success_page, name='success_page'),  # 成功ページのURL
]