from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def sendTickers(request):
    response = request.POST
    ticker1 = response['ticker1']
    ticker2 = response['ticker2']
    print(ticker1, ticker2)
    return JsonResponse({'success':True})
