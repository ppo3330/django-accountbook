from django.shortcuts import render
from .models import Record

def record_list(request):
    records = Record.objects.all().order_by('-date', '-id')

    return render(request, 'accountbook/list.html', {
        'records': records
    })