#!/usr/bin/ python
#Random Zip Code generator
import requests
import random
import sys

# API endpoint to get the location for a US zip code
location_api = "https://api.zippopotam.us/us/{}"\

# Zip code entered as the argument
zip_code = sys.argv[1]

# Generate a random number between 0 and 4 to change a digit of the zip code
random_index = random.randint(0, 4)

# Convert the zip code to a list of characters so we can modify a single digit              
zip_code_list = list(zip_code)

# Change one digit of the zip code
old_zip_code = zip_code
new_zip_code = "".join(zip_code_list[:random_index] + [str(random.randint(0, 9))] + zip_code_list[random_index + 1:])

# Get the location for the old zip code
response = requests.get(location_api.format(old_zip_code))
if response.status_code == 404:
    print(f"Old zip code {old_zip_code} not found.")
    sys.exit(1)
old_location = response.json()

# Get the location for the new zip code
response = requests.get(location_api.format(new_zip_code))
if response.status_code == 404:
    print(f"New zip code {new_zip_code} not found.")
    sys.exit(1)
new_location = response.json()

# Print the old and new zip codes and their locations
print(f"Old zip code: {old_zip_code} - {old_location['places'][0]['place name']}, {old_location['places'][0]['state']}")
print(f"New zip code: {new_zip_code} - {new_location['places'][0]['place name']}, {new_location['places'][0]['state']}")
