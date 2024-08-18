from django.http import HttpResponse

def home(request):
    return HttpResponse("Merhaba! Bu softalya backend projesinin ana sayfasıdır.")
