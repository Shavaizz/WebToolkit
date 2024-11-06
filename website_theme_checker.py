import requests
from dotenv import load_dotenv
import os
load_dotenv()

apikey = os.environ['apikey']
def main():
    if not apikey:
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
        webwithouthttp = website_checker_url.lstrip("http://").lstrip("https://")
        response = requests.get(f"https://www.themedetect.com/API/Theme?url={webwithouthttp}&key={apikey}")

        response.raise_for_status()


        parsed_data = response.json()


        if 'result' in parsed_data and parsed_data['result'].get('code') == 200:
            results = parsed_data.get('results', [])
            if not results:
                print("No theme information found for this website.")
            else:
                for technology in results:
                    name = technology.get('theme_name', 'Unknown')
                    license = technology.get('license', 'Unknown')
                    print(f"Theme Name: {name}, Version: {license}")
        else:
            print(f"Error: Failed to retrieve valid theme information (Code: {parsed_data['result'].get('code', 'N/A')})")
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to make request to API. Details: {e}")
    except ValueError:
        print("Error: Failed to parse JSON response from the API.")
    except Exception as e:
        print(f"Unexpected error: {e}")