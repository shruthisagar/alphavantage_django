from django.http import HttpResponse
from datetime import datetime
import requests
from django.http.response import JsonResponse
from alpha.models import AlphavantageData
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
import redis

@csrf_exempt
def handle_request(request):
    if request.method=="GET":
        
        data = list(AlphavantageData.objects.filter().values())
        return JsonResponse(data, safe=False)
 
    # data = requests.get("https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=BTC&market=USD&interval=60min&apikey=96IF88GOW43ZTHRG").json()
    res = AlphavantageData(
        open_value=55.5,
        low_value=15.5,
        close_value=35.5,
        high_value=125.5,
        created_time=datetime.utcnow(),
        volume_value=100
    ).save()
    cache.hmset(dict(open_value=55.5,
        low_value=15.5,
        close_value=35.5,
        high_value=125.5,
        created_time=datetime.utcnow(),
        volume_value=100))
    return JsonResponse({
        "name": "sagar"
    })