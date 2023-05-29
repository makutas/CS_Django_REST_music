from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_bands),
    path('add_band/', views.add_band),
    path('band/<int:pk>', views.get_specific_band),
    path('update_band/<int:pk>', views.update_specific_band),
    path('delete_band/<int:pk>', views.delete_band),
]