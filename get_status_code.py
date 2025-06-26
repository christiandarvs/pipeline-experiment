import requests

try:
    response = requests.get("https://www.google.com")
    status_code = response.status_code
    print(f"Status code for Google: {status_code}")

    response_404 = requests.get("https://www.example.com/nonexistent-page")
    status_code_404 = response_404.status_code
    print(f"Status code for a nonexistent page: {status_code_404}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
