from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from .models import *


def home_view(request):
    return HttpResponse("""
    <h1>Salom hammaga</h1>
    """)

def home_page(request):
    return render(request,'home.html')

def muallif_list(request):

    if request.method == "POST":
        Muallif.objects.create(
            ism = request.POST.get('ism'),
            jins = request.POST.get('jins'),
            tugilgan_sana = request.POST.get('tugilgan_sana'),
            tirik = request.POST.get('tirik') if request.POST.get('tirik') else 0,
            kitob_soni=request.POST.get('kitob_soni') if request.POST.get('kitob_soni') else 0
        )
        return redirect('/muallif/')

    mualliflar = Muallif.objects.all()
    eng_katta = Muallif.objects.order_by("-kitob_soni")[:3]
    katta_yosh = Muallif.objects.order_by("tugilgan_sana")[:3]
    eng_kop_kitob = Muallif.objects.filter(kitob_soni__lt=10)
    search = request.GET.get('search')

    if search:
        mualliflar = mualliflar.filter(ism__contains=search)

    context = {
        'mualliflar' : mualliflar,
        'eng_katta' : eng_katta,
        'katta_yosh' : katta_yosh,
        'eng_kop_kitob' : eng_kop_kitob,
        'search':search,
    }
    return render(request,"muallif.html", context=context)

def muallif_confirm_delete_view(request, pk):
    muallif = get_object_or_404(Muallif, pk=pk)
    context = {
        'muallif':muallif,
    }
    return render(request, "muallif_confirm_delete.html", context=context)


def muallif_delete(request,pk):
    muallif = get_object_or_404(Muallif,pk=pk)
    muallif.delete()
    return redirect("/muallif/")


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
    if request.method == 'POST':
        muallif = get_object_or_404(Muallif, id=request.POST.get('muallif_id'))
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            janr=request.POST.get('janr'),
            sahifa=request.POST.get('sahifa'),
            muallif= muallif,
        )
        return redirect('/kitob/')

    kitoblar = Kitob.objects.all()
    authors = Muallif.objects.all()
    sahifalar = Kitob.objects.order_by ("-sahifa")[:3]
    badiiylar = Kitob.objects.filter(janr="badiiy")

    ordering = request.GET.get('ordering')
    if ordering:
        kitoblar = kitoblar.order_by(ordering)

    sahifa = request.GET.get('sahifa')
    if sahifa:
        kitoblar = kitoblar.order_by(sahifa)
    context = {
        'kitoblar':kitoblar,
        'sahifalar': sahifalar,
        'badiiylar': badiiylar,
        'ordering': ordering,
        'sahifa':sahifa,
        'authors':authors,
    }
    return render(request,"kitob.html", context=context)

def tanlangan_kitob_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob':kitob,
    }
    return render(request,"tanlangan-kitob.html", context=context)

def record_view(request):

    if request.method == 'POST':
        Record.objects.create(
            talaba = get_object_or_404(Talaba, id=request.POST.get('talaba_id')),
            kitob = get_object_or_404(Kitob, id=request.POST.get('kitob_id')),
            admin = get_object_or_404(Admin, id=request.POST.get('admin_id')),
            olingan_sana = request.POST.get('olingan_sana'),
            qaytatrish_sanasi = request.POST.get('qaytatrish_sanasi'),
        )
        redirect('/recosd/')
    recordlar = Record.objects.all()
    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    adminlar = Admin.objects.all()
    record_sana = Record.objects.order_by("-olingan_sana")[:3]
    bitiruvchilar = Record.objects.filter(talaba__kurs=4)
    search = request.GET.get('search')

    if search:
        recordlar = recordlar.filter(talaba__ism__contains=search)

    context = {
        "recordlar":recordlar,
        'record_sana':record_sana,
        'bitiruvchilar' : bitiruvchilar,
        'search':search,
        'talabalar':talabalar,
        'kitoblar':kitoblar,
        'adminlar':adminlar,
    }
    return render(request,"record.html", context = context)

def record_delete_confirm_view(request,pk):
    record = get_object_or_404(Record,pk=pk)
    context = {
        "record":record,
    }
    return render(request, "record_delete_confirm.html", context=context)


def record_delete_view(request,pk):
    record = get_object_or_404(Record,pk=pk)
    record.delete()
    return redirect("/record/")

def tirik_view(request):
    tiriklar = Muallif.objects.filter(tirik=True)
    tirik_kitoblar = Kitob.objects.filter(muallif__tirik=True)
    context = {
        'tiriklar':tiriklar,
        'tirik_kitoblar' : tirik_kitoblar,
    }
    return render(request,"tirik.html", context=context)

def talaba_view(request):

    if request.method == 'POST':
        Talaba.objects.create(
            ism=request.POST.get('ism'),
            guruh = request.POST.get('guruh'),
            kurs = request.POST.get('kurs'),
            kitob_soni = request.POST.get('kitob_soni') if request.POST.get('kitob_soni') else 0
        )
        return redirect('/talaba/')
    talabalar = Talaba.objects.all()
    ordering = request.GET.get('ordering')
    if ordering:
        talabalar = talabalar.order_by(ordering)

    kurs = request.GET.get('kurs')
    if kurs:
        talabalar = talabalar.filter(kurs=kurs)

    context = {
        'talabalar': talabalar,
        'ordering':ordering,
        'kurs':kurs
    }
    return render(request, "talaba.html", context=context)

def admin_view(request):
    if request.method =='POST':
        Admin.objects.create(
            ism = request.POST.get('ism'),
            ish_vaqti = request.POST.get('ish_vaqti'),
        )
        return redirect('/admin_view/')
    adminlar = Admin.objects.all()
    context = {
        'adminlar':adminlar,
    }
    return render(request, 'admin_view.html', context=context)


