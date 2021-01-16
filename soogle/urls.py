from django.urls import path
from .views import index, PostView

app_name = 'soogle'

urlpatterns = [
    path('post/', PostView.as_view(), name='post')
]