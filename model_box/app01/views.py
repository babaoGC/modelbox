from django.shortcuts import render,HttpResponse

from rest_framework.views import APIView
from app01.box_forms import BoxForm
from rest_framework.response import Response


# Create your views here.


class Register(APIView):

    def get(self,request,*args,**kwargs):
        form_obj = BoxForm()
        return render(request,'register.html',locals())

    def post(self,request,*args,**kwargs):
        return Response('ok')






