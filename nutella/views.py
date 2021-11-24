from django.shortcuts import render
from off.fetcher import ApiConsulter


# Create your views here.
def index(request):
    ApiConsulter.db_save()
    return render(request,'index.html')
