from django.urls import include, path
from rest_framework import routers
from musicapp import views

router = routers.DefaultRouter()
router.register(r'artistes', views.ArtisteViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'lyrics', views.LyricsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
