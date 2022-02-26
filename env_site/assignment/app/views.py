from urllib import request
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import StockData
# Create your views here.
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Hello, ' + request.user.first_name}
        return Response(content)

# class DashboardView(APIView):
#     permission_classes = (IsAuthenticated, )

#     def get(self, request):
#         content = {'message': 'Hello, ' + request.user.first_name}
#         return Response(content)


def dashboardView(request):
    context = {}
    return render(request, "dashboard/dashboard.html", context)
    # if request.user.is_authenticated:
    #     return render(request, "dashboard/dashboard.html", context)
    # else:
    #     return redirect('token_obtain_pair')


def stocksData(request):
    stocks = request.POST.getlist('stocks[]')
    stocks_data = StockData.objects.all().values()
    graphs_data = []
    for each in stocks:
        single_row = {}
        single_row['type'] = "line"
        single_row['axisYType'] = "secondary"
        single_row['name'] = each
        single_row['showInLegend'] = True
        single_row['markerSize'] = 0
        single_row['yValueFormatString'] = "#,###"
        single_row['dataPoints'] = []
        for st in stocks_data:
            st_single = {}
            st_single['x'] = st["date"].strftime("%Y-%m-%d")
            st_single['y'] = st[each]
            single_row['dataPoints'].append(st_single)
        graphs_data.append(single_row)
    return JsonResponse({'graphs_data': graphs_data})
