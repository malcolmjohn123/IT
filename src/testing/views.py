from django.shortcuts import render, HttpResponse
from django.views import View
from .models import *


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

class CCMember_claims(View):
    def get(self, request):
        template_name = 'ccmembers_claims.html'

        # context = { 'ccmember' : TestingClaims.objects.raw('select distinct a.memid ,a.id from testing_claims a\
        #                                                     left join testing_elig b\
        #                                                     on a.memid=b.memid\
        #                                                     where b.memid is null'),
        #             'ddmember': TestingClaims.objects.raw('select distinct a.memid as memid,a.id from testing_elig a\
        #                                                             left join testing_claims b\
        #                                                             on a.memid=b.memid\
        #                                                             where b.memid is null'),
        #             'matched': TestingClaims.objects.raw('select distinct a.memid as memid,a.id from testing_claims a\
        #                                                                     join testing_elig b\
        #                                                                     on a.memid=b.memid')
        #             }
        context = { 'claims':TestingClaims.objects.raw('select distinct memid,id from testing_claims'),
                    'elig':TestingElig.objects.raw('select distinct memid,id from testing_elig'),
                    'matched': TestingClaims.objects.raw('select distinct a.memid as memid,a.id from testing_claims a\
                                                                                    join testing_elig b\
                                                                                     on a.memid=b.memid'),
                    'ccmember': TestingClaims.objects.raw('select a.lvlid2,a.id, count(distinct memid) as memcount from testing_claims a \
                                                        left join testing_elig b\
                                                        on a.memid=b.memid\
                                                         where b.memid is null\
                                                         group by a.lvlid2,a.id')
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
                    'ccmember': TestingClaims.objects.raw('select a.lvlid2,a.id, count(distinct memid) as memcount from testing_rxclaims a \
                                                left join testing_elig b\
                                                on a.memid=b.memid\
                                                 where b.memid is null\
                                                 group by a.lvlid2,a.id')
        }
        return render(request, template_name, context)
