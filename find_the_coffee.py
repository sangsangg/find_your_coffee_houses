#!/usr/bin/env python3
"""find the coffee house that you love"""
import json
import requests


token = "AIzaSyD-qaaNkokKbMqltsBKJ5A4YWwnFr_OQBc"


def define_location():
    name = input("Hi there! Where are you right now?: ")
    name = name.replace(" ", "+")
    location_url = ("https://maps.googleapis.com/maps/api/"
                    "geocode/json?address={}&key={}").format(name, token)
    json_type = requests.get(location_url).json()

    latitude = json_type['results'][0]['geometry']['location']['lat']
    longtitude = json_type['results'][0]['geometry']['location']['lng']

    location = (str(latitude) + ", " + str(longtitude))

    return location


def radius():
    """"N" MUST BE in kilometers type, both int and float are accepted."""
    length = float(
        input("Let me help you find some coffee, the radius from there?: "))
    try:
        if type(length) is int or float:
            distance = int(length * 1000)
    except ValueError:
        print('Type again the length in kilometers '
              'that you want to find your coffee house')

    return distance


def location_data():
    location = define_location()
    length = radius()
    find_coffee_url = ("https://maps.googleapis.com/maps/"
                       "api/place/nearbysearch/json?location={}&radius={}"
                       "&types=cafe&name=coffee&key={}").format(location,
                                                                length, token)
    data = requests.get(find_coffee_url).json()

    print("Good news!! I got some for you!")

    for result in data['results']:
        coffee_data = result['name'], result['rating'], result['vicinity']
        print(coffee_data)
    return "Thanks for asking!!! ^^ Have a nice day!!"


def main():
    location_data()
    with open("coffee_house.json", "w") as f:
        json.dump(location_data, f)


if __name__ == '__main__':
    main()
