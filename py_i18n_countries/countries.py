import json

nationalities = None


def load(locale):
    global nationalities
    with open(f"iso-3166-1/{locale}.json") as json_file:
        data = json.load(json_file)
        nationalities = data["nationalities"]


def get_nationality(code, locale="en"):
    global nationalities
    if nationalities == None:
        load(locale)
    try:
        return nationalities[code]
    except LookupError:
        print(f"Did not find a country for code: {code}")
