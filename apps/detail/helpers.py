from .models import JurnalDetail
from django.shortcuts import render


def count_detail(jurnal_id):
    list_debt = []
    list_kredit = []


    detail = JurnalDetail.objects.filter(jurnal_id=jurnal_id)
    print(detail)
    for d in detail:
        de = int(float(d.debt))
        kr = int(float(d.kredit))
        list_debt.append(de)
        list_kredit.append(kr)

    total_debt = sum(list_debt)
    total_kredit = sum(list_kredit)


    return total_debt,total_kredit