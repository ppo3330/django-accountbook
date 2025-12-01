from django.shortcuts import render, redirect, get_object_or_404
from .models import Record

def record_list(request):
    records = Record.objects.all().order_by('-date', '-id')

    return render(request, 'accountbook/list.html', {
        'records': records
    })

def record_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        record_type = request.POST.get('record_type')
        category = request.POST.get('category')
        date = request.POST.get('date')

        if title and amount and record_type and category and date:
            Record.objects.create(
                title=title,
                amount=amount,
                record_type=record_type,
                category=category,
                date=date,
            )
            return redirect('record_list')
    return render(request, 'accountbook/record_form.html')

def record_detail(request,pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'accountbook/detail.html',{
        'record':record
    })