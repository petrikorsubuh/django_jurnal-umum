from django.db import models
from apps.jurnal import models as mj


class JurnalDetail(models.Model):
    jurnal = models.ForeignKey(mj.Jurnal, on_delete=models.CASCADE,related_name='details')
    tanggal = models.DateField(auto_now=False,auto_now_add=False)
    deskripsi = models.CharField(max_length=100)
    kredit = models.CharField(max_length=20,default=0.0,blank=True)
    debt = models.CharField(max_length=20,default=0.0,blank=True)

    def __str__(self):
        return self.deskripsi

    class Meta:
        db_table = 'detail'
        ordering =['-id']
