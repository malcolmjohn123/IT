from django.shortcuts import render, HttpResponse
from django.views import View
from .models import TestingClaims, TestingElig, TestingRxclaims


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



class MemberMatch(View):
    def get(self, request):
        template_name = 'membermatch.html'
        return render(request, template_name, {})

class LoaTestCase(View):
    def get(self, request):
        template_name = 'loatestcase.html'
        return render(request, template_name, {})


class MmEm(View):
    def get(self, request):
        template_name = 'mmem.html'
        mem = TestingElig.objects.raw('select 1 as id, count(distinct memid) memcount, count(distinct enrid) enridcount, cast(effdate as month) as month from testing_elig group by cast(effdate as month)')
        return render(request, template_name, {'mem':mem})



class CCMember_claims(View):
    def get(self, request):
        template_name = 'ccmembers_claims.html'
        context = { 'claims':TestingClaims.objects.raw('select distinct memid,id from testing_claims'),
                    'elig':TestingElig.objects.raw('select distinct memid,id from testing_elig'),
                    'matched': TestingClaims.objects.raw('select distinct a.memid as memid,a.id from testing_claims a\
                                                                                    join testing_elig b\
                                                                                     on a.memid=b.memid'),
                    'ccmember': TestingClaims.objects.raw('select a.lvlid2 as lvl,1 as a.id, count(distinct a.memid) as memcount from testing_claims a \
                                                        left join testing_elig b\
                                                        on a.memid=b.memid\
                                                         where b.memid is null\
                                                         group by lvlid2,id')
        }
        return render(request, template_name, context)
class CCMember_rxclaims(View):
    def get(self, request):
        template_name = 'ccmembers_rxclaims.html'
        context = { 'rxclaims':TestingRxclaims.objects.raw('select distinct memid,id from testing_rxclaims'),
                    'elig':TestingElig.objects.raw('select distinct memid,id from testing_elig'),
                    'matched': TestingRxclaims.objects.raw('select distinct a.memid as memid,a.id from testing_rxclaims a\
                                                                                    join testing_elig b\
                                                                                     on a.memid=b.memid'),
                    'ccmember': TestingClaims.objects.raw('select a.lvlid2 as lvlid2 ,1 as a.id, count(distinct memid) as memcount from testing_rxclaims a \
                                                left join testing_elig b\
                                                on a.memid=b.memid\
                                                 where b.memid is null\
                                                 group by a.lvlid2,a.id')
        }
        return render(request, template_name, context)









