from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', home_view),
    path('', home_page),
    path('muallif/', muallif_list),
    path("muallif/<int:muallif_id>/", tanlangan_view),
    path('muallif/<int:pk>/update/', muallif_update),
    path("muallif/<int:pk>/delete/confirm/", muallif_confirm_delete_view),
    path("muallif/<int:pk>/delete/", muallif_delete),
    path('kitob/', kitob_view),
    path("kitob/<int:kitob_id>/", tanlangan_kitob_view, name="tanlangan_kitob"),
    path("kitob/<int:pk>/delete/", kitob_delete),
    path("kitob/<int:pk>/delete/confirm/", kitob_delete_confirm),
    path("kitob/<int:pk>/update/", kitob_update),

    path("record/", record_view),
    path("record/<int:pk>/delete/confirm/", record_delete_confirm_view),
    path("record/<int:pk>/delete/", record_delete_view),
    path("tirik/", tirik_view),
    path("record/<int:record_id>/", tanlangan_record_view, name="tanlangan_record_view"),
    path('record/<int:pk>/update/', record_update),
    path('talaba/', talaba_view),
    path('talaba/<int:pk>/', talaba_tanlangan),
    path('talaba/<int:pk>/update/', talaba_update),
    path('talaba/<int:pk>/delete/', talaba_delete),
    path('talaba/<int:pk>/delete/confirm/', talaba_delete_confirm),
    path('admin_view/', admin_view),
    path('admin_view/<int:pk>/', tanlangan_admin),
    path('admin_view/<int:pk>/delete/', admin_delete),
    path('admin_view/<int:pk>/delete/confirm', admin_delete_confirm),
    path('admin_view/<int:pk>/update', admin_update),
]
