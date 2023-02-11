from django.shortcuts import redirect, render
import requests
# Create your views here.
# Crypto currency updated with javascript others django

def getCurrency(name,date_start,date_end):
    data = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{name}/range/1/day/{date_start}/{date_end}?apiKey=ZNwiXVfaDev8Ik2GXLQ0SsisKB6yBdKD")
    data = data.json()
    if data["status"] == "ERROR":
        return "   Our Free Services Limited By 1 minute You can buy me a coffee for more!"
    return data['results'][0]["c"]

def getBtcCurrency(id, len):
    data = requests.get("https://api.coincap.io/v2/assets")

    if data.text=="You exceeded your 200 request(s) rate limit of your FREE plan":
            return "   Our Free Services Limited By 1 minute You can buy me a coffee for more!"

    data = data.json()

    data = data["data"]
    prc = float(str((data[id - 1]["priceUsd"]))[:len])

    return prc

def mainCurrency(id):
    # id == 0 DOLAR id == 1 EURO
    text = "USD_TRY"
    if id == 1:
        text = "EUR_TRY"
    data = requests.get(f"https://free.currconv.com/api/v7/convert?q={text}&compact=ultra&apiKey=bd0dd3713dff14e2e75e")

    if "503" in data.text:
        return 16 if id == 0 else 17
   
    prc = int((data.json())[text])
    return prc
        

def main(request):

    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "index.html",context={
        "AAPL":getCurrency("AAPL","2022-05-27","2022-05-31"),
        "MSFT":getCurrency("MSFT","2022-05-27","2022-05-31"),
        "GOOGL":getCurrency("GOOGL","2022-05-27","2022-05-31"),
        "AMZN":getCurrency("AMZN","2022-05-27","2022-05-31"),
        "XP":getCurrency("XP","2022-05-27","2022-05-31"),

        "BTC":getBtcCurrency(1,5),
        "ETH":getBtcCurrency(2,4),
        "XRP":getBtcCurrency(7,5),
        "ADA":getBtcCurrency(6,5),
        "SHIB":getBtcCurrency(16,5),

        "DOLAR":mainCurrency(0),
        "EUR":mainCurrency(1),

    })