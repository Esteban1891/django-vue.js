from django.urls import path
from apps.facturaxion import views 
 
urlpatterns = [ 
    path('api/getFacturaxion/', views.facturaxion_list),
    path('api/createFacturaxion/', views.facturaxion_create),
]