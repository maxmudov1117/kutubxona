from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=255)
    kurs = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])
    kitob_soni = models.PositiveIntegerField()

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=255, choices=(('erkak','erkak'),('ayol','ayol')))
    tugilgan_sana = models.DateTimeField()
    kitob_soni = models.PositiveIntegerField()
    tirik = models.BooleanField(default=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = 'Muallif'
        verbose_name_plural = 'Mualliflar'

class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=255)
    sahifa = models.PositiveIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete = models.CASCADE,)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'

class Admin(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.CharField(max_length=255)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Adminlar'

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE,)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE,)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE,)
    olingan_sana = models.DateTimeField()
    qaytatrish_sanasi = models.DateField()

    def __str__(self):
        return f"{self.talaba} - {self.kitob} - {self.admin}"




