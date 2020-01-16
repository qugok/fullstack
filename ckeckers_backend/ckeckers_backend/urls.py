"""ckeckers_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    url(r'^', include('ckeckers_api.urls')),
    url(r'^my_api/', include('ckeckers_api.urls')),
    url(r'^admin/', admin.site.urls),
]

# {"data": {"time": {"updated": "Dec 10, 2019 16:46:00 UTC", "updatedISO": "2019-12-10T16:46:00+00:00",
#                    "updateduk": "Dec 10, 2019 at 16:46 GMT"},
#           "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
#           "chartName": "Bitcoin", "bpi": {
#         "USD": {"code": "USD", "symbol": "&#36;", "rate": "7,231.3550", "description": "United States Dollar",
#                 "rate_float": 7231.355},
#         "GBP": {"code": "GBP", "symbol": "&pound;", "rate": "5,490.3484", "description": "British Pound Sterling",
#                 "rate_float": 5490.3484},
#         "EUR": {"code": "EUR", "symbol": "&euro;", "rate": "6,520.7514", "description": "Euro",
#                 "rate_float": 6520.7514}}}, "status": 200, "statusText": "",
#  "headers": {"content-type": "application/javascript", "cache-control": "max-age=15", "content-length": "672",
#              "expires": "Tue, 10 Dec 2019 16:48:07 UTC"},
#  "config": {"transformRequest": {}, "transformResponse": {}, "timeout": 0, "xsrfCookieName": "XSRF-TOKEN",
#             "xsrfHeaderName": "X-XSRF-TOKEN", "maxContentLength": -1,
#             "headers": {"Accept": "application/json, text/plain, */*"}, "method": "get",
#             "url": "https://api.coindesk.com/v1/bpi/currentprice.json"}, "request": {}}
