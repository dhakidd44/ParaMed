from django.contrib import admin
from django.urls import path, include
from myApp.views import PatientAPIView
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import routers
 
from myApp.views import PatientAPIView
 
# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘patient’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/patient/’
router.register('patient', PatientAPIView, basename='patient')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myApp.urls")),
    path('api/patient/', PatientAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))  # Il faut bien penser à ajouter les urls du router dans la liste des urls disponibles.
]
