from django.urls import path
from . import views

urlpatterns = [
   path('hello/', views.hello, name='hello'),
   path('',views.home, name='home'),
   path('update/<int:id>',views.update_view, name='update'),
]