from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    date = datetime.today()
    context = {"pseudo": "Pyt", "date": date}
    return render(request=request,
                  template_name="index.html",
                  context=context)
