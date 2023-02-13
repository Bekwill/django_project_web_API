from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', views.NoteViewSet, basename='note')
urlpatterns = [
    #path('', views.NoteCollectionView.as_view()),
    #path('<int:pk>/', views.NoteSingletoView.as_view())
] + router.urls

# urlpatterns = router.urls