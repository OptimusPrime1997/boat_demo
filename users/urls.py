from django.conf.urls import url

import users.views

urlpatterns = [
    url(r'^search_tonnage/(?P<content>.*)$', users.views.search_tonnage),
    url(r'^search_tonnage_data/(?P<content>.*)$', users.views.search_tonnage_data),
    url(r'^search_cargo/(?P<content>.*)$', users.views.search_cargo),
    url(r'^search_tc/(?P<content>.*)$', users.views.search_tc),
    url(r'^cargo$', users.views.get_cargo),
    url(r'^tonnage$', users.views.get_tonnage),
    url(r'^tc$', users.views.get_tc),

    # query
    url(r'^tonnage_search$', users.views.tonnage_card_search, ),
    url(r'^cargo_search$', users.views.cargo_card_search, ),
    url(r'^tc_search$', users.views.tc_card_search, ),

    #search incomplete
    url(r'^ton_incomplete$', users.views.tonnage_card_incomplete, ),
    #search complete
    url(r'^ton_complete$', users.views.tonnage_card_complete, ),

    #search incomplete
    url(r'^car_incomplete$', users.views.cargo_card_incomplete, ),
    #search complete
    url(r'^car_complete$', users.views.cargo_card_complete, ),

    #search incomplete
    url(r'^tc_incomplete$', users.views.tc_card_incomplete, ),
    #search complete
    url(r'^tc_complete$', users.views.tc_card_complete, ),

    #update
    url(r'^tc_update$', users.views.tc_update, ),
    url(r'^tonnage_update$', users.views.tonnage_update, ),
    url(r'^cargo_update$', users.views.cargo_update, ),

    #flag
    url(r'^ton_flag$', users.views.ton_flag, ),
    url(r'^tc_flag$', users.views.tc_flag, ),
    url(r'^cargo_flag$', users.views.cargo_flag, ),

    # change date
    url(r'^ton_date$', users.views.ton_date),
    url(r'^cargo_date', users.views.cargo_date),
    url(r'^tc_date', users.views.tc_date),

]