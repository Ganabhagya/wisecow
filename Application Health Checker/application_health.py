import requests
from datetime import datetime

def check_application_health(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        if status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return 'down'

def log_application_status(url, status):
    with open('application_health_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()}: Application at {url} is {status}\n")

def main():
    url = "http://example.com"  # Replace with your application's URL
    status = check_application_health(url)
    print(f"Application at {url} is {status}")
    log_application_status(url, status)

if __name__ == "__main__":
    main()