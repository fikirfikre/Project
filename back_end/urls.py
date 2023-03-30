from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.Home.as_view()),
    path('news_list/', views.NewsList.as_view()),
    path('news_list/<int:pk>', views.NewsDetail.as_view()),
    path('service_list/', views.ServiceList.as_view()),
    path('service_list/<int:pk>', views.ServiceDetail.as_view()),
    path('institution_list/', views.InstitutionList.as_view()),
    path('institution_list/<int:pk>', views.InstitutionDetail.as_view()),

]
