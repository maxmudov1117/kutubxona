from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from .forms import *
from .models import *


def home_view(request):
    return HttpResponse("""
    <h1>Salom hammaga</h1>
    """)


def home_page(request):
    return render(request, 'home.html')


def muallif_list(request):
    if request.method == "POST":
        data = MuallifForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/muallif/')

    mualliflar = Muallif.objects.all()
    eng_katta = Muallif.objects.order_by("-kitob_soni")[:3]
    katta_yosh = Muallif.objects.order_by("tugilgan_sana")[:3]
    eng_kop_kitob = Muallif.objects.filter(kitob_soni__lt=10)
    search = request.GET.get('search')

    if search:
        mualliflar = mualliflar.filter(ism__contains=search)

    context = {
        'mualliflar': mualliflar,
        'eng_katta': eng_katta,
        'katta_yosh': katta_yosh,
        'eng_kop_kitob': eng_kop_kitob,
        'search': search,
        'form': MuallifForm(),
    }
    return render(request, "muallif.html", context=context)


def muallif_confirm_delete_view(request, pk):
    muallif = get_object_or_404(Muallif, pk=pk)
    context = {
        'muallif': muallif,
    }
    return render(request, "muallif_confirm_delete.html", context=context)


def muallif_delete(request, pk):
    muallif = get_object_or_404(Muallif, pk=pk)
    muallif.delete()
    return redirect("/muallif/")


def muallif_update(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)

    if request.method == 'POST':
        form = MuallifForm(request.POST, instance=muallif)
        if form.is_valid():
            form.save()
            return redirect('/muallif/')

    context = {
        'muallif': muallif,
        'form': MuallifForm(instance=muallif),
    }

    return render(request, "muallif_update.html", context=context)


def tanlangan_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        'muallif': muallif,
    }
    return render(request, "tanlangan.html", context)


def tanlangan_record_view(request, record_id):
    record = Record.objects.get(id=record_id)
    context = {
        'record': record,
    }
    return render(request, "tanlangan-record.html", context)


def kitob_view(request):
    form = KitobForm()
    if request.method == 'POST':
        data = KitobForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/kitob/')

    kitoblar = Kitob.objects.all()
    authors = Muallif.objects.all()
    sahifalar = Kitob.objects.order_by("-sahifa")[:3]
    badiiylar = Kitob.objects.filter(janr="badiiy")

    ordering = request.GET.get('ordering')
    if ordering:
        kitoblar = kitoblar.order_by(ordering)

    sahifa = request.GET.get('sahifa')
    if sahifa:
        kitoblar = kitoblar.order_by(sahifa)
    context = {
        'kitoblar': kitoblar,
        'sahifalar': sahifalar,
        'badiiylar': badiiylar,
        'ordering': ordering,
        'sahifa': sahifa,
        'authors': authors,
        'form': form,
    }
    return render(request, "kitob.html", context=context)


def kitob_delete(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    kitob.delete()
    return redirect("/kitob/")


def kitob_delete_confirm(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)
    context = {
        'kitob': kitob,
    }
    return render(request, "kitob_delete_confirm.html", context=context)


def kitob_update(request, pk):
    kitob = get_object_or_404(Kitob, pk=pk)

    if request.method == 'POST':
        form = KitobForm(request.POST, instance=kitob)
        if form.is_valid():
            form.save()
            return redirect('/kitob/')

    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
        'kitob': kitob,
        'form': KitobForm(instance=kitob),
    }
    return render(request, "kitob_update.html", context=context)


def tanlangan_kitob_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob': kitob,
    }
    return render(request, "tanlangan-kitob.html", context=context)


def record_view(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/record/')
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
        "recordlar": recordlar,
        'record_sana': record_sana,
        'bitiruvchilar': bitiruvchilar,
        'search': search,
        'talabalar': talabalar,
        'kitoblar': kitoblar,
        'adminlar': adminlar,
        'form': RecordForm(),
    }
    return render(request, "record.html", context=context)


def record_delete_confirm_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    context = {
        "record": record,
    }
    return render(request, "record_delete_confirm.html", context=context)


def record_delete_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    record.delete()
    return redirect("/record/")


def record_update(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/record/')

    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    adminlar = Admin.objects.all()

    context = {
        'talabalar': talabalar,
        'kitoblar': kitoblar,
        'adminlar': adminlar,
        'record': record,
        'form': RecordForm(instance=record),
    }
    return render(request, "record_update.html", context=context)


def tirik_view(request):
    tiriklar = Muallif.objects.filter(tirik=True)

    tirik_kitoblar = Kitob.objects.filter(muallif__tirik=True)
    context = {
        'tiriklar': tiriklar,
        'tirik_kitoblar': tirik_kitoblar,
    }
    return render(request, "tirik.html", context=context)


def talaba_view(request):
    form = TalabaForm()
    if request.method == 'POST':
        form = TalabaForm(request.POST)
        if form.is_valid():
            form.save()
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
        'ordering': ordering,
        'kurs': kurs,
        'form': form,
    }
    return render(request, "talaba.html", context=context)


def talaba_tanlangan(request, pk):
    talaba = Talaba.objects.get(id=pk)

    context = {
        'talaba': talaba,
    }
    return render(request, "tanlangan_talaba.html", context=context)


def talaba_delete(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk)
    talaba.delete()
    return redirect('/talaba/')


def talaba_delete_confirm(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk)

    context = {
        'talaba': talaba,
    }

    return render(request, "talaba_confirm_delete.html", context=context)


def talaba_update(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    if request.method == 'POST':
        form = TalabaForm(request.POST, instance=talaba)
        if form.is_valid():
            form.save()
            return redirect('/talaba/')

    context = {
        'talaba': talaba,
        'form': TalabaForm(instance=talaba),
    }
    return render(request, 'talaba_update.html', context=context)


def admin_view(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_view/')

    adminlar = Admin.objects.all()
    context = {
        'adminlar': adminlar,
        'form': AdminForm(),
    }
    return render(request, 'admin_view.html', context=context)


def tanlangan_admin(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    context = {
        'admin': admin,
    }
    return render(request, "tanlangan_admin.html", context=context)


def admin_delete(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    admin.delete()
    return redirect('/admin_view/')


def admin_delete_confirm(request, pk):
    admin = get_object_or_404(Admin, pk=pk)

    context = {
        'admin': admin,
    }
    return render(request, "admin_confirm.html", context=context)


def admin_update(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    if request.method == 'POST':
        form = AdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('/admin_view/')

    context = {
        'admin': admin,
        'form': AdminForm(instance=admin),
    }
    return render(request, "admin_update.html", context=context)
