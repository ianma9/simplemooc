from django.urls import include, path
from simplemooc.core import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),  
]
 