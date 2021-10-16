from alpha.models import AlphavantageBTCtoUSD
from django.core.cache import cache
import requests
from django.forms.models import model_to_dict
from alphavantage import settings


def get_latest_data():
    # data = list(AlphavantageData.objects.filter().values())
    data = cache.get("alphavantageBTCtoUSD")
    if not data:
        data = AlphavantageBTCtoUSD.objects.only(
            "exchange_rate", "last_refresh_time"
        ).last()
        data = model_to_dict(data)
        cache.set("alphavantageBTCtoUSD", data)
        if not data:
            store_latest_data()
    return data


def store_latest_data():
    _url = (
        "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey="
        + settings.ALPHAVANTAGE_ACCESS_KEY
    )
    data = requests.get(_url).json()
    data = data["Realtime Currency Exchange Rate"]

    res = AlphavantageBTCtoUSD(
        exchange_rate=data["5. Exchange Rate"],
        last_refresh_time=data["6. Last Refreshed"],
    ).save()

    res = cache.set(
        "alphavantageBTCtoUSD",
        dict(
            exchange_rate=data["5. Exchange Rate"],
            last_refresh_time=data["6. Last Refreshed"],
        ),
    )
    return {"status": 1}
