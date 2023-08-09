import csv
import json
import zipfile
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Equity

def extract_ohlc(request):
    # url = '.https://www.bseindia.com/download/BhavCopy/Equity/EQ070823_CSV.zip'
    # response = requests.get(url)

    # print(response.status_code, response.headers.get('content-type'))

    zip_file_path = './EQ070823_CSV.zip'

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('.')

    csv_file_path = './EQ070823.CSV'

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            Equity.objects.create(
                code = row[0],
                name = row[1],
                open = row[4],
                high = row[5],
                low = row[6],
                close = row[7]
            )

    return HttpResponse("Bhavcopy parsed and saved to DB")


def equity_list(request):
    equities = Equity.objects.all()
    search_query = request.GET.get('search', '')
    equities = Equity.objects.filter(name__icontains = search_query)
    return render(request, 'equity_list.html', {'equities': equities, 'search_query': search_query})


def download_csv(request):
    search_query = request.GET.get('search', '')
    equities = Equity.objects.filter(name__icontains = search_query)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="searchResult.csv"'

    csv_writer = csv.writer(response)
    csv_writer.writerow(['Code', 'Name', 'Open', 'High', 'Low', 'Close'])

    for equity in equities:
        csv_writer.writerow([equity.code, equity.name, equity.open, equity.high, equity.low, equity.close])

    return response


def update_equity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data['code']

        equities = Equity.objects.filter(code=code)
        for equity in equities:
            for field, value in data['data'].items():
                setattr(equity, field, value)
            equity.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


def delete_equity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data['code']

        equity = Equity.objects.filter(code = code)
        equity.delete()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})



