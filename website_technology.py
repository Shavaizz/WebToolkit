import requests
from dotenv import load_dotenv
from website_theme_checker import main as webtheme
import time
load_dotenv()
import os
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
        webwithouthttp = website_checker_url
        response = requests.get(f"https://whatcms.org/API/Tech?key={apikey}&url={webwithouthttp}")
        response.raise_for_status()
        parsed_data = response.json()
        wordpress_found = False
        if 'result' in parsed_data and parsed_data['result'].get('code') == 200:
            results = parsed_data.get('results', [])
            if not results:
                print("No technologies detected for this website.")
            else:
                print("Technologies Detected: ")
                for technology in results:
                    name = technology.get('name', 'Unknown')
                    version = technology.get('version', 'N/A')
                    category = technology.get('categories', 'N/A')
                    print(f"Name: {name}, Version: {version}, Used As: {category}")
                    if name == "WordPress":
                        wordpress_found = True
                if wordpress_found:
                    print("Theme Detection Activated")
                    time.sleep(10)
                    webtheme()
                else:
                    return
        else:
            print(f"Error: Failed to retrieve valid technology information (Code: {parsed_data['result'].get('code', 'N/A')})")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to make request to API. Details: {e}")
    except ValueError:
        print("Error: Failed to parse JSON response from the API.")
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":
    main()
