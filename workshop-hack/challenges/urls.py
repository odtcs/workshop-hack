from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^1$', Challenge01View.as_view(), name='1'),
    url(r'^2$', Challenge02View.as_view(), name='2'),
    url(r'^3$', Challenge03View.as_view(), name='3'),
    url(r'^4$', Challenge04View.as_view(), name='4'),
    url(r'^5$', Challenge05View.as_view(), name='5'),
    url(r'^6$', Challenge06View.as_view(), name='6'),
    url(r'^7$', Challenge07View.as_view(), name='7'),
]
