from django.shortcuts import render
import csv


def read_csv():

    with open(file='C:/Users/79055/PycharmProjects/django3/task1/inflation_russia.csv', encoding='utf-8') as \
            csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        reader_sorted = []
        for row in reader:
            tmp = row[0].split(';')
            reader_sorted.append(tmp)
    return reader_sorted.pop(0), reader_sorted


def inflation_view(request):

    headers, csv = read_csv()
    context = {'csv': csv, 'headers': headers}

    return render(request, 'inflation.html',
                  context)
