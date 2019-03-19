from django.conf.urls import url

import users.views

urlpatterns = [
    url(r'^search_cargo/(?P<content>.*)$', users.views.search_cargo),
    url(r'^search_tonnage/(?P<content>.*)$', users.views.search_tonnage),
    url(r'^search_tc/(?P<content>.*)$', users.views.search_tc),
    url(r'^cargo$', users.views.get_cargo),
    url(r'^tonnage$', users.views.get_tonnage),
    url(r'^tc$', users.views.get_tc),

]