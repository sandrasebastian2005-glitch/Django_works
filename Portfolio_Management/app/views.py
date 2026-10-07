from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.

class Aboutapi(View):
    def get(self,request):
        data={"id":101,"full name":"Sandra Sebastian","title":"About Me","DOB":"23-08-2005","Email":"sandrasebastian2005@gmail.com","contact":"9700673580","location":"ekm","github url":"","linkedin url":""}
        return JsonResponse(data)

class Educationapi(View):
    def get(self,request):
        data={"id":101,"institution":"ASAS","Course":"BCA","University":"Amrita Vishwa Vidyapeetham","location":"ekm","start year":"2023","End Year":"2026","Grade":"A","Description":"nyc"}
        return JsonResponse(data)

class Projectsapi(View):
    def get(self,request):
        data=[{"id":1,"projectname":"bookinn","description":"hotel booking management","technologies":"python,flask,react,html,api","duration":"1 month","liveurl":" "},
              {"id":2,"projectname":"cognifit","description":"health management","technologies":"python,,react,html,css","duration":"1 month","liveurl":" "}]
        return JsonResponse(data,safe=False)