from django.db import models
from autoslug import AutoSlugField

class yazi(models.Model):
    baslik = models.CharField(max_length=120)
    ozet = models.TextField(max_length=300)
    icerik = models.TextField()
    olustuma_tarihi = models.DateTimeField(auto_now_add=True)
    gunselleme_tarihi = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='baslik', unique=True, editable=False)
    class Meta:
        db_table = 'yazilar'       #veritabanının ismini belirler