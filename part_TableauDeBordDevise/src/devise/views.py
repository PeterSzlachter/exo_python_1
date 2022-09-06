from django.shortcuts import render, redirect
import api
from datetime import date, datetime, timedelta

liste_nb = [1, 2, 3, 4, 5]

def redirect_index(request):
    return redirect('home', days_range=30, currencies="HUF,USD")

def dashboard(request, days_range=30, currencies="CAD"):

    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalisé")
    for day in days:
        index = days.index(day)
        day = datetime.strptime(day, "%Y-%m-%d").date()
        day = day.strftime("%d %B %Y")
        days[index] = day
    return render(request, "devise/index.html",context={"data": rates,
                                                        "days_labels": days,
                                                        "currencies": currencies,
                                                        "page_label": page_label})
