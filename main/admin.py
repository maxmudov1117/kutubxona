from django.contrib import admin
from main.models import *
from django.contrib.auth.models import Group, User
from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model


class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id', 'guruh', 'ism', 'kurs', 'kitob_soni')
    list_display_links = ('id', 'guruh')
    search_fields = ('ism', 'guruh')


class FoydalanuvchiAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'ish_vaqti')
    list_editable = ('ism', 'ish_vaqti')
    list_filter = ('ish_vaqti',)
    list_ordering = ('ism',)
    list_per_page = 3
    search_fields = ('ism',)


class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'jins', 'tugilgan_sana', 'kitob_soni', 'tirik',)
    search_fields = ('ism',)
    list_filter = ('tirik',)
    list_display_links = ('id', 'ism',)
    list_editable = ('kitob_soni', 'tirik',)


class KitobAdmin(admin.ModelAdmin):
    search_fields = ('nom', 'muallif__ism')  # muallifga bog'liq maydonni ham qidirish mumkin
    list_display = ('nom', 'janr', 'sahifa', 'muallif')

class RecordAdmin(admin.ModelAdmin):
    search_fields = ('talaba', 'kitob', 'admin',)
    list_display = ("talaba", "kitob", "admin", "olingan_sana", "qaytatrish_sanasi",)
    date_hierarchy = 'olingan_sana'
    autocomplete_fields = ['talaba', 'kitob', 'admin']
    fields = ("talaba", "kitob", "admin", "olingan_sana", "qaytatrish_sanasi")



admin.site.unregister([Group, User])
admin.site.register(Admin, FoydalanuvchiAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kitob,KitobAdmin)
admin.site.site_header = 'Kutubxona admin paneli'
admin.site.site_title = 'Kutubxona boshqaruvi'
admin.site.index_title = 'Kutubxona'
admin.site.empty_value_display = "Ma'lumot yo'q"
