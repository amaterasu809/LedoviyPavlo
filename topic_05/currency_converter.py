import requests

request = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

currency = input("\nEnter currency(1, 2 or 3):\n 1. USD \n 2. EUR \n 3. PLN \n")
if currency == "1":
    currency = "USD"
elif currency == "2":
    currency = "EUR"
elif currency == "3":
    currency = "PLN"
else: 
    print("Wrong input!")
    
for elem in request.json():
    if elem["cc"] == currency:
        rate = elem["rate"]
        break

amount = float(input("Enter amount of currency to convert to UAH: "))

print(amount, currency, " = ", rate*amount, "UAH")