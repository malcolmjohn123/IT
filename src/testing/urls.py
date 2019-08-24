
from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'visualization'

urlpatterns = [
    path('', Homepage.as_view(), name = 'homepage'),
    path('login/', Login.as_view(), name = 'login'),
    path('ccmemberclaims/', CCMember_claims.as_view(), name = 'ccmembersclaims'),
    path('ccmemberrxclaims/', CCMember_rxclaims.as_view(), name='ccmembersrxclaims'),

]
