
from django.contrib import admin
from django.urls import path
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', home_view),
    path('', home_page),
    path('muallif/', muallif_list),
    path("muallif/<int:muallif_id>/",tanlangan_view ),
    path("muallif/<int:pk>/delete/confirm/",muallif_confirm_delete_view ),
    path("muallif/<int:pk>/delete/",muallif_delete ),
    path('kitob/',kitob_view),
    path("kitob/<int:kitob_id>/",tanlangan_kitob_view, name="tanlangan_kitob"),
    path("record/", record_view),
    path("record/<int:pk>/delete/confirm/", record_delete_confirm_view),
    path("record/<int:pk>/delete/", record_delete_view),
    path("tirik/", tirik_view),
    path("order/<int:record_id>/",tanlangan_record_view, name="tanlangan_record_view")
]
