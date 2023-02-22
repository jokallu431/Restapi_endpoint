import csv
from operator import itemgetter
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import CsvDataSerializer
from django.contrib import messages
from django.shortcuts import redirect, render

def services(request):
     
     global attributeid

     if request.method == 'POST':
          uploaded_file = request.FILES['file']
          print(uploaded_file)
          attributeid= request.POST.get('attributeid')
          print(attributeid)
          if uploaded_file.name.endswith('.csv'):
               
               return redirect(csv_data)
          else: 
               messages.warning(request,'File was not uploaded. Please use csv file extension!')
     return render (request,'services.html')


@api_view(['GET'])
def csv_data(request):
#     csv_file = open('C:/Users/H P/Desktop/miniproject/DataVisualization/media/Cars93.csv')
    csv_file = read_csv()
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader]
    sorted_data = sorted(data, key=itemgetter(attributeid))
    serializer = CsvDataSerializer(sorted_data, many=True)
    return JsonResponse(serializer.data, safe=False)

def read_csv():
    csv_file = open('C:/Users/H P/Desktop/miniproject/DataVisualization/media/Cars93.csv')
    return csv_file

