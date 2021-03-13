from django.conf.urls import url
from qa.views import test

urlpatterns = [
    url(r'^$', test),
    url(r'^popular/.*$', test),    
    url(r'^ask/.*$', test),
    url(r'^answer/.*$', test),
    url(r'^signup/.*$', test),
    url(r'^login/.*$', test),
    url(r'^logout/.*$', test),    
    url(r'^new/.*$', test),
    url(r'^question/(?P<question_id>[0-9]+)/$', test),    
]