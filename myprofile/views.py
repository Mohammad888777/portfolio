from django.shortcuts import render,redirect,get_object_or_404
from django.views import View

from .models import Profile



class Home(View):


    def get(self,request,*args,**kwargs):   

        context={
            'name':"mohammad"
        }

        return render(request,"index.html",context)