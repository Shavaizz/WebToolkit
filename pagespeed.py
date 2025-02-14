import requests
from dotenv import load_dotenv
load_dotenv()
import os
apikey = os.environ["google_pagespeed_api"]
def desktop_speed_getter():
    try:
        response = requests.get(f"https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed/?url=https://time.com")
        response.raise_for_status()
        parsed_data = response.json()
        overall_score = parsed_data.get("loadingExperience", {}).get("overall_category", "Key not found")
        print(f"Overall Average Speed For Desktop: {overall_score}")
    except Exception as e:
        print(f"Error Occured: {e}")
def mobile_speed_getter():
    try:
        response = requests.get(f"https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed/?strategy=MOBILE&url=https://time.com")
        response.raise_for_status()
        parsed_data = response.json()
        overall_score = parsed_data.get("loadingExperience", {}).get("overall_category", "Key not found")
        print(f"Overall Average Speed For Mobile: {overall_score}")
    except Exception as e:
        print(f"Error Occured: {e}")
def main():
    if not apikey:
        print("Error: API key is missing. Please make sure the API key is set in your .env file.")
        return
    # try:
    #     with open("website.txt", "r") as file:
    #         website_checker_url = file.read().strip()
    #     if not website_checker_url:
    #         print("Error: Website URL is missing. Please make sure the Website URL is set in your .env file.")
    # except Exception as e:
    #     print(f"Error Occured When Making Request: {e}")
    try:
        # webwithouthttp = website_checker_url
        print("Executing Here, about to fetch speed for mobile users")
        desktop_speed_getter()
        mobile_speed_getter()
    except ValueError:
        print("Error: Failed to parse JSON response from the API.")
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":
    main()
