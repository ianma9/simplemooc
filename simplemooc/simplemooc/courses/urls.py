from django.urls import include, path
from simplemooc.courses import views
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:pk>/', views.details, name='details'),
    path('<slug>/', views.details, name='details'),

]
 