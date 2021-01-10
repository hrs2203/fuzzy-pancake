from django.urls import path, include

import responseBot.views as fxn


urlpatterns = [
    path("compareQuery", fxn.CompareQuery.as_view(), name='compareQuery'),
]
    
