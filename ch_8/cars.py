def make_car_dict(manuf, model, **car_info):
    car_dict = {"manufacturer": manuf, "model": model}
    for key, val in car_info.items():
        car_dict[key] = val
    return car_dict


car_stats = make_car_dict(
    "dodge", "ram 1500", trim="rebel", suspension="air", stereo_watts=1000
)
for stat in car_stats:
    print(car_stats[stat])
