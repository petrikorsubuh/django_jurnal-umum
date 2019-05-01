from django.db import models
from django.contrib.auth.models import User


class Jurnal(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='jurnals')
    nama = models.CharField(max_length=25)
    keterangan = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'jurnal'
        ordering =['-id']
