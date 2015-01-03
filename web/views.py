# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from gm_pr import settings, chan_proj
from gm_pr.PrFetcher import PrFetcher
import time

def index(request):
    projects, channel = chan_proj.chan_proj(request)

    if projects != None:
        before = time.time()

        prf = PrFetcher(settings.TOP_LEVEL_URL, settings.ORG, projects)
        context = {"project_list" : prf.get_prs()}

        after = time.time()
        print(after - before)
        return render(request, 'pr.html', context)
    else:
        return HttpResponse("No project found\n", status=404)