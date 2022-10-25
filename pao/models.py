from tabnanny import verbose
from django.db import models

# Create your models here.
class Tracker(models.Model):

    nobody = models.IntegerField(verbose_name = "Не согласовано никем")
    soglDecan = models.IntegerField(verbose_name = "Согласовано только деканами")
    decanFinans = models.IntegerField(verbose_name = "Требуют финансирования (задачи деканов)")
    bezRectorVisa = models.IntegerField(verbose_name = "Без визы ректора")
    paoCan = models.IntegerField(verbose_name = "Может согласовать ПАО")

    naSoglDecan = models.IntegerField(verbose_name = "На согласовании деканов")
    fbp = models.IntegerField(verbose_name = "ФБП")
    fgs = models.IntegerField(verbose_name = "ФГС")
    fcep = models.IntegerField(verbose_name = "ФКЭП")
    uf = models.IntegerField(verbose_name = "ЮФ")

    remake = models.IntegerField(verbose_name = "Отправлено на доработку")
    remakeDecan = models.IntegerField(verbose_name = "Отправлено на доработку деканами")
    remakeAup = models.IntegerField(verbose_name = "Отправлено на доработку АУП")
    remakeRector = models.IntegerField(verbose_name = "Отправлено на доработку ректором")

    naSoglAdv = models.IntegerField(verbose_name = "На согласовании ООС")
    naSoglProdject = models.IntegerField(verbose_name = "На согласовании проектного")
    naSoglYung = models.IntegerField(verbose_name = "На согласовании молодежной политики")
    naSoglLearn = models.IntegerField(verbose_name = "На согласовании молодежной учебная деятельность")
    naSoglHr = models.IntegerField(verbose_name = "На согласовании HR")
    naSoglScience = models.IntegerField(verbose_name = "На согласовании наука")
    naSoglredact = models.IntegerField(verbose_name = "На согласовании редакционный отдел")


