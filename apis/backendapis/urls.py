from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('upload', views.FileUploadViewset, basename='upload')
# router.register('download', views.DownloadView, basename='download')

urlpatterns = [
    path('', include(router.urls)),
    # path('upload/', views.FileUploadViewset.as_view({'get': 'list', 'post': 'create'}), name='upload'),
    path('download/', views.DownloadView.as_view(), name='download'),
    path('delete/', views.DeleteView.as_view(), name='delete'),
]




