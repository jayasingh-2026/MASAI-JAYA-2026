import requests

# Dummy API key (for demonstration)
api_key = "12345abcde_dummy_key"

# API endpoint
url = "https://api.example.com/data"

# Headers with Authorization Bearer token
headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    # Send GET request
    response = requests.get(url, headers=headers)

    # Handle status codes
    if response.status_code == 200:
        print(response.json())

    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")

    else:
        print("Request failed", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error occurred while making request:", e)
