from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^home$', HomeView.as_view(), name='home'),
    url(r'^check$', CheckView.as_view(), name='check'),
    url(r'^challenge/', include('challenges.urls'), name='challenges')
]
