from datetime import datetime
import requests
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from alpha.controllers import get_latest_data, store_latest_data


@csrf_exempt
def handle_request(request):
    if request.method == "GET":
        data = get_latest_data()
        return JsonResponse(data, safe=False)

    response = store_latest_data()
    return JsonResponse(response, safe=False)
