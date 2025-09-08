from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import *

def home_view(request):
    return HttpResponse("""
    <h1>Salom hammaga</h1>
    """)

def home_page(request):
    return render(request,'home.html')

def muallif_list(request):
    mualliflar = Muallif.objects.all()
    eng_katta = Muallif.objects.order_by("-kitob_soni")[:3]
    katta_yosh = Muallif.objects.order_by("tugilgan_sana")[:3]
    eng_kop_kitob = Muallif.objects.filter(kitob_soni__lt=10)
    context = {
        'mualliflar' : mualliflar,
        'eng_katta' : eng_katta,
        'katta_yosh' : katta_yosh,
        'eng_kop_kitob' : eng_kop_kitob,
    }
    return render(request,"muallif.html", context=context)

def tanlangan_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        'muallif' : muallif,
    }
    return render(request, "tanlangan.html", context)

def tanlangan_record_view(request, record_id):
    records = Record.objects.get(id=record_id)
    context = {
        'records' : records,
    }
    return render(request, "tanlangan.html", context)

def kitob_view(request):
    kitoblar = Kitob.objects.all()
    sahifalar = Kitob.objects.order_by ("-sahifa")[:3]
    badiiylar = Kitob.objects.filter(janr="badiiy")
    context = {
        'kitoblar':kitoblar,
        'sahifalar': sahifalar,
        'badiiylar': badiiylar
    }
    return render(request,"kitob.html", context=context)

def tanlangan_kitob_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob':kitob,
    }
    return render(request,"tanlangan-kitob.html", context=context)

def record_view(request):
    recordlar = Record.objects.all()
    record_sana = Record.objects.order_by("-olingan_sana")[:3]
    bitiruvchilar = Record.objects.filter(talaba__kurs=4)
    context = {
        "recordlar":recordlar,
        'record_sana':record_sana,
        'bitiruvchilar' : bitiruvchilar,
    }
    return render(request,"record.html", context = context)

def tirik_view(request):
    tiriklar = Muallif.objects.filter(tirik=True)
    tirik_kitoblar = Kitob.objects.filter(muallif__tirik=True)
    context = {
        'tiriklar':tiriklar,
        'tirik_kitoblar' : tirik_kitoblar,
    }
    return render(request,"tirik.html", context=context)

