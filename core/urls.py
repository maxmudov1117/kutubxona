
from django.contrib import admin
from django.urls import path
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', home_view),
    path('', home_page),
    path('muallif/', muallif_list),
    path("muallif/<int:muallif_id>/",tanlangan_view ),
    path('kitob/',kitob_view),
    path("kitob/<int:kitob_id>/",tanlangan_kitob_view, name="tanlangan_kitob"),
    path("record/", record_view),
    path("tirik/", tirik_view),
    path("order/<int:record_id>/",tanlangan_record_view, name="tanlangan_record_view")
]
