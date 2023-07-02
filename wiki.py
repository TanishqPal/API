import requests

# URL of the Wikipedia API endpoint
url = "https://en.wikipedia.org/w/api.php"

# Parameters for the API request
params = {
    "action": "query",
    "format": "json",
    "prop": "extracts",
    "exintro": False,
    "explaintext": True,
    "titles": "India"
}

# Send the API request
response = requests.get(url, params=params)
data = response.json()

# Extract the page extract from the response
page_id = next(iter(data['query']['pages']))  # Get the page ID
page_extract = data['query']['pages'][page_id]['extract']  # Get the page extract

# Print the page extract
print(data)
