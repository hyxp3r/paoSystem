
from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
class Tracker(models.Model):

    createdTime = models.DateTimeField(auto_now_add=True)
    nobody = models.IntegerField(verbose_name = "Не согласовано никем", default = 0)
    soglDecan = models.IntegerField(verbose_name = "Согласовано только деканами", default = 0)
    decanFinans = models.IntegerField(verbose_name = "Требуют финансирования (задачи деканов)", default = 0)
    bezRectorVisa = models.IntegerField(verbose_name = "Без визы ректора" , default = 0)
    paoCan = models.IntegerField(verbose_name = "Может согласовать ПАО", default = 0)

    naSoglDecan = models.IntegerField(verbose_name = "На согласовании деканов", default = 0)
    fbp = models.IntegerField(verbose_name = "ФБП", default = 0)
    fgs = models.IntegerField(verbose_name = "ФГС", default = 0)
    fcep = models.IntegerField(verbose_name = "ФКЭП", default = 0)
    uf = models.IntegerField(verbose_name = "ЮФ", default = 0)

    remake = models.IntegerField(verbose_name = "Отправлено на доработку", default = 0)
    remakeDecan = models.IntegerField(verbose_name = "Отправлено на доработку деканами", default = 0)
    remakeAup = models.IntegerField(verbose_name = "Отправлено на доработку АУП", default = 0)
    remakeRector = models.IntegerField(verbose_name = "Отправлено на доработку ректором", default = 0)

    naSoglAdv = models.IntegerField(verbose_name = "На согласовании ООС", default = 0)
    naSoglProdject = models.IntegerField(verbose_name = "На согласовании проектного", default = 0)
    naSoglYung = models.IntegerField(verbose_name = "На согласовании молодежной политики", default = 0)
    naSoglLearn = models.IntegerField(verbose_name = "На согласовании молодежной учебная деятельность", default = 0)
    naSoglHr = models.IntegerField(verbose_name = "На согласовании HR", default = 0)
    naSoglScience = models.IntegerField(verbose_name = "На согласовании наука", default = 0)
    naSoglredact = models.IntegerField(verbose_name = "На согласовании редакционный отдел", default = 0)

    class Meta:

        verbose_name = 'Трекер'
        verbose_name_plural = 'Трекер'

    def __str__(self) -> str:
        return (self.createdTime.strftime("%d-%m-%Y %H:%M:%S") )