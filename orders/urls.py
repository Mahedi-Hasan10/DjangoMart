from django.urls import path
from . import views
urlpatterns = [
    path('order_completed/',views.complete_order,name='complete_order'),
    path('place_order/',views.place_order,name='place_order'),
    path('success/', views.success_view, name='success_view'),
]