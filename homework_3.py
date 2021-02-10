"""● Să se scrie un program care conține următoarele funcționalități:
○ citește datele de intrare dintr-un fișier aflat în fișierul input .csv
○ generează un folder output_data care va conține următoarele fișiere .json:
➠ slow_cars.json - conține datele despre toate mașinile care se încadrează în categoria slow_cars.
➠ fast_cars.json - conține datele despre toate mașinile care se încadrează în categoria fast_cars.
➠ sport_cars.json - conține datele despre toate mașinile care se încadrează în categoria sport_cars.
➠ cheap_cars.json - conține datele despre toate mașinile care se încadrează în categoria cheap.
➠ medium_cars.json - conține datele despre toate mașinile care se încadrează în categoria medium.
➠ expensive_cars.json - conține datele despre toate mașinile care se încadrează în categoria expensive.
➠ câte un fișier care conține toate datele despre un anumit brand de mașină. Ex: opel.json va conține toate datele
despre mașinile al căror proprietate brand are valoarea Opel.
● La o rulare a programului, output-ul va fi valabil DOAR pentru datele curente. Fișierele vechi nu vor trebui să existe."""

import csv
import json
from pprint import pprint
from pathlib import Path
import shutil

_ID = 0
my_list = []


def get_new_id():

    global _ID
    _ID += 1
    return _ID


def csv_unpacking(car_list):

    for f in car_list:

        my_dict = {"id": get_new_id(), "brand": f[0], "model": f[1], "hp": f[2],
                   "price": f[3]}
        my_list.append(my_dict)
    return my_list


cars = []

with open("input.csv") as csv_file:
    my_data = list(csv.reader(csv_file))
    header = my_data[0]
    statistics = my_data[1:]
    for data in statistics:
        cars.append(data)


cars = csv_unpacking(cars)
dir_name = "output_data"
p = Path() / dir_name
if p.exists():
    shutil.rmtree(p)
p.mkdir(exist_ok=True)


with open(p/"slow_cars.json", "w") as file:
    slow_cars = json.dumps([car for car in cars if int(car["hp"]) < 120])
    file.write(slow_cars)
with open(p/"fast_cars.json", "w") as file:
    fast_cars = json.dumps(
        [car for car in cars if 120 <= int(car["hp"]) < 180])
    file.write(fast_cars)
with open(p/"sports_cars.json", "w") as file:
    sports_cars = json.dumps(
        [car for car in cars if int(car["hp"]) >= 180])
    file.write(sports_cars)
with open(p/"cheap_cars.json", "w") as file:
    cheap_cars = json.dumps(
        [car for car in cars if int(car["price"]) < 1000])
    file.write(cheap_cars)
with open(p/"affordable_cars.json", "w") as file:
    affordable_cars = json.dumps([car for car in cars if
                                  1000 <= int(car["price"]) <= 5000])
    file.write(affordable_cars)
with open(p/"expensive_cars.json", "w") as file:
    expensive_cars = json.dumps(
        [car for car in cars if int(car["price"]) > 5000])
    file.write(expensive_cars)
brands = [brand["brand"] for brand in cars]

for car_brand in brands:
    brand_json = json.dumps([car for car in cars if car_brand == car["brand"]])
    file_name = car_brand + ".json"
    with open(p/ file_name, "w") as file:
        file.write(brand_json)
