from django.shortcuts import render, HttpResponse
from django.views import View
from .models import TestingClaims


# Create your views here.

# class Homepage(View):
#     def get(self, request):
#         return HttpResponse('Here in homepage !!')


class Homepage(View):
    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name, {})


class Login(View):
    def get(self, request):
        template_name = 'login.html'
        return render(request, template_name, {})


class CCMember(View):
    def get(self, request):
        template_name = 'ccmembers.html'
        return render(request, template_name, {})


