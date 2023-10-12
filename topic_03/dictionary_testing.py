car = {
    'model': 'RAV4',
    'engine': '2.0'
}

car.update({'VIN': '2165981981651816'})
print(car)

del car["engine"]
print(car)

car.clear()
print(car)

car.keys()
car["model"] = "Prius"
print(car)

car.values()
car["model"] = "CH-R"
print(car)

car.items()
car["engine"] = "1.6"
print(car)

