import requests
import os
from dotenv import load_dotenv
load_dotenv()

rapidapikey = os.environ['rapidapikey']

def main():
    if not rapidapikey:
        print("Error: API key is missing. Please make sure the API key is set in your .env file.")
        return
    try:
        with open("website.txt", "r") as file:
            website_checker_url = file.read().strip()
        if not website_checker_url:
            print("Error: The website URL in 'website.txt' is empty. Please add a valid URL.")
            return
    except FileNotFoundError:
        print("Error: 'website.txt' not found. Please make sure the file exists.")
        return
    except Exception as e:
        print(f"Unexpected error reading 'website.txt': {e}")
        return
    try:
        webwithouthttp = website_checker_url
        url = "https://whois-lookup-api.p.rapidapi.com/domain-age"

        querystring = {"domain":f"https://www.{webwithouthttp}/","format":"days"}

        headers = {
            "x-rapidapi-key": f"{rapidapikey}",
            "x-rapidapi-host": "whois-lookup-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        results = response.json()
        creation_date = results.get('creation', 'N/A') 
        domain_age_days = results.get('age', 'N/A')
        print(f"Creation Date: {creation_date} Domain Age: {domain_age_days}")
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to make request to API. Details: {e}")
    except ValueError:
        print("Error: Failed to parse JSON response from the API.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
if __name__ == "__main__":
    main()