# The Python standard library includes some functionality for communicating
# over the Internet.
# However, we will use a more powerful and simpler library called requests.
# This is external library that you may need to install first.
import requests


def get_data():
    # With requests, we can ask the web service for the data.
    # Can you understand the parameters we are passing here?
    response = requests.get(
        "http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
        params={
            'starttime': "2000-01-01",
            "maxlatitude": "58.723",
            "minlatitude": "50.008",
            "maxlongitude": "1.67",
            "minlongitude": "-9.756",
            "minmagnitude": "1",
            "endtime": "2018-10-11",
            "orderby": "time-asc"}
    )

    # The response we get back is an object with several fields.
    # The actual contents we care about are in its text field:
    text = response.text
    # To understand the structure of this text, you may want to save it
    # to a file and open it in VS Code or a browser.
    # See the README file for more information.
    # We need to interpret the text to get values that we can work with.
    # What format is the text in? How can we load the values?
    return json.loads(response.text)


def count_earthquakes(earthquake_data):
    """Get the total number of earthquakes in the response."""
    # len(earthquake_data['features'])
    return len(earthquake_data['features'])


def get_magnitude(earthquake_no):
    """Retrive the magnitude of an earthquake item."""
    return earthquake_data['features'][earthquake_no]['properties']['mag']


def get_location(earthquake):
    """Retrieve the latitude and longitude of an earthquake item."""
    # There are three coordinates, but we don't care about the third (altitude)
    return ...


def get_maximum(data):
    """Get the magnitude and location of the strongest earthquake in the data."""
    ...


# With all the above functions defined, we can now call them and get the result
earthquake_data = get_data()
print(f"Loaded {count_earthquakes(data)}")




max_magnitude, max_location = get_maximum(data)
print(f"The strongest earthquake was at {max_location} with magnitude {max_magnitude}")






#######################
# exploration
import requests
response = requests.get(
        "http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
        params={
            'starttime': "2000-01-01",
            "maxlatitude": "58.723",
            "minlatitude": "50.008",
            "maxlongitude": "1.67",
            "minlongitude": "-9.756",
            "minmagnitude": "1",
            "endtime": "2018-10-11",
            "orderby": "time-asc"}
    )

    # The response we get back is an object with several fields.
    # The actual contents we care about are in its text field:
text = response.text
type(text)
len(text)

#text_clean = text.strip()
import json
earthquake_data = json.loads(response.text)
type(earthquake_data)
len(earthquake_data)
print (earthquake_data)

# formatting nicely as a file
with open('earthquake_data3.json', 'w') as file:
    json.dump(earthquake_data, file, indent=4, sort_keys=True)




# trying to parse the data
import pandas as pd

"""
sunspots = pd.read_csv(spots.raw, delimiter=';',
                       names=['year','month','date',
                               'mean','deviation','observations','definitive'])
"""

earthquake_data = pd.read_json(text)
earthquake_data = pd.read_json(text_clean)
type(earthquake_data)
print(earthquake_data['bbox'])
print(earthquake_data['features']['100'])
print(earthquake_data['features'][1])
earthquake_list = earthquake_data['features']
len(earthquake_list)
earthquake_data['features'][5]['properties']['mag']
print(earthquake_data['features'][1]['properties']['mag'])


for n in range(119):
    print(earthquake_data['features'][n]['properties']['mag'])
    
    # magnitude.append(earthquake_data['features'][n]['properties']['mag'])

    earthquake_data['features'][1]['properties']['mag'])


 