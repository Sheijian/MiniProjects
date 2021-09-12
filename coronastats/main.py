from covid import Covid
import matplotlib.pyplot as pyplot

covid = Covid()
print("Want data of specific country (press: 1)")
print("World data (press: 2)")
ch = int(input("Enter your choice: "))
if ch == 1:
    country = input("Enter your country name: ")
    data = covid.get_status_by_country_name(country)
    cadr = {
        key: data[key]
        for key in data.keys() & {"confirmed", "active", "deaths", "recovered"}
    }
    n = list(cadr.keys())
    v = list(cadr.values())
elif ch == 2:
    cadr = {
        "confirmed": covid.get_total_confirmed_cases(),
        "active": covid.get_total_active_cases(),
        "deaths": covid.get_total_deaths(),
        "recovered": covid.get_total_recovered(),
    }
    v = list(cadr.values())
    n = list(cadr.keys())

    print(cadr)
    pyplot.title("Corona Tracker")
    pyplot.bar(range(len(cadr)), v, tick_label=n)
    pyplot.show()
