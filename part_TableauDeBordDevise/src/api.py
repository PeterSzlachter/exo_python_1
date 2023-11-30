from datetime import date, timedelta
from pprint import pprint
import requests


# https://www.frankfurter.app/docs/

def get_rates(currencies, days=30, base_curr="EUR"):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)
    symbols = ','.join(currencies)
    # requete = f"https://api.frankfurter.app/&start_date={start_date}&end_date={end_date}&currencies={symbols}"
    requete = f"https://api.frankfurter.app/{start_date}..{end_date}?to={symbols}&from=USD"

    r = requests.get(requete)
    # test = r.json()
    if not r and not r.json():
        return False, False

    api_rates = r.json().get("rates")
    all_rates = {currency: [] for currency in currencies}
    all_days = sorted(api_rates.keys())

    for each_day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]

    return all_days, all_rates


if __name__ == '__main__':
    days, rates = get_rates(["USD"])
    pprint(days)
    # pprint(rates)
