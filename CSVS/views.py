from django.shortcuts import render
from numpy import product
from .forms import CsvModelForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from sales.models import Sale


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    product = row[1].upper()
                    user = User.objects.get(username=row[3])
                    Sale.objects.create(
                        product=product,
                        quantity=int(row[2]),
                        salesmen=user,
                    )
            obj.activated = True
            obj.save()
    return render(request, 'CSVS/upload.html', {'form': form})