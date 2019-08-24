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
        context = TestingClaims.objects.raw('select LVLID2, LVLDESC2, MEMID,sum(paidamt) as paidamt from testing_claims a\
                                                where not exists (select 1 from testing_elig b\
                                                where a.memid=b.memid)\
                                                group by LVLID2, LVLDESC2, MEMID')

        return render(request, template_name, {'context': context})


class Login(View):
    def get(self, request):
        template_name = 'login.html'
        return render(request, template_name, {})



