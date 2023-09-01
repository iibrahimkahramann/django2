from django.db import models
from autoslug import AutoSlugField

class yazi(models.Model):
    baslik = models.CharField(max_length=120)
    ozet = models.TextField(max_length=300)
    icerik = models.TextField()
    olustuma_tarihi = models.DateTimeField(auto_now_add=True)
    gunselleme_tarihi = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='baslik', unique=True, editable=True, blank=True)         #UNİQUE admin panelde kullanıp kullanılmayacagını soyler   #blank zorunlu doldurmayı kapatır
    yazar = models.CharField(max_length=1200, null=True)   #sonradan olusturdugumuz kolon veritabanını bozmasın diye null kullanıyoruz boş olabilir diyoruz
    class Meta:
        db_table = 'yazilar'      #veritabanının ismini belirler
        verbose_name = 'yazi'
        verbose_name_plural = 'Yazılar'

    def __str__(self):
        return self.baslik


