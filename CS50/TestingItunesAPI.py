import requests

# GET request to GeeksforGeeks
get_response = requests.get("https://www.geeksforgeeks.org/")

# Printing only the status code
print(get_response.status_code)
