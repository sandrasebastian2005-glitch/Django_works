from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View

class Studentdetails(View):
    def get(self,request):
        data={"studname":"Sandra","age":22,"Course":"Python","mark":89}
        return JsonResponse(data)

class Studentlist(View):
    def get(self,request):
        data=[{"studname":"Sandra","age":22,"Course":"Python","mark":89},
              {"studname":"Ayana","age":22,"Course":"Python","mark":91},
              {"studname":"Fathima","age":21,"Course":"Python","mark":90}]
        return JsonResponse(data,safe=False)

    