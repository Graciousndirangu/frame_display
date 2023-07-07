from django.urls import path
from . import views

app_name = 'frames'

urlpatterns = [
    path('', views.frame_view, name='frame_view'),
    path('<int:frame_id>/', views.display_urls, name='display_urls'),
]
