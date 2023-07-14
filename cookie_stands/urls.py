from django.urls import path
from .views import CookieStandDetail , CookieStandList

urlpatterns = [
    path("", CookieStandList.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="cookie_stand_detail"),
]
