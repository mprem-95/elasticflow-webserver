from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import orchestrator.utils.cache_utils as cache
import orchestrator.utils.airflow_utils as airflow_utils
import orchestrator.utils.constants as constants

import json


def index(request):

    commodity = request.GET.get("commodity")
    state = request.GET.get("state")
    region = request.GET.get("region")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    apmc = request.GET.get("apmc")
    news = request.GET.get("news")
    sector = request.GET.get("sector")
    social_media = request.GET.get("social_media")
    politics = request.GET.get("politics")
    nature = request.GET.get("nature")
    global_cues = request.GET.get("global_cues")

    print("Values Received : ")

    print(str(commodity) + str(state) + " " + str(region) + " " + str(start_date) + " " + str(end_date) + " " + str(apmc) + " "
          + str(news) + " " + str(sector) + " " +  str(social_media) + " " + str(politics) + " "
          + str(nature) + " " + str(global_cues))

    configuration = {
                    "meta" : {
                       "commodity": commodity,
                       "state": state,
                       "region": region,
                       "start_date": start_date,
                       "end_date": end_date

                    },
                    "sources" : [apmc, news, sector, social_media, politics, nature, global_cues],
    }

    cache.set("configuration", json.dumps(configuration))

    print("From Cache : " + str(cache.get("configuration")))
    configuration_cached = cache.get("configuration")
    configuration_cached = json.loads(configuration_cached)
    print(configuration_cached["sources"])

    airflow_utils.trigger_airflow_dag(constants.DAG_ID)

    return HttpResponse("<br><br><br><h2 align ='center'>ElasticFlow Configured Successfully</h2>")
