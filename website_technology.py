import requests
from dotenv import load_dotenv
load_dotenv()
import os
apikey = os.environ['apikey']
def main():
    try:
        with open("website.txt", "r") as file:
            website_checker_url = file.read().strip()
    except FileNotFoundError:
        print("No website URL found. Please run the first script.")

    webwithouthttp = website_checker_url
    print(webwithouthttp)
    jsonrequest = requests.get(f"https://whatcms.org/API/Tech?key={apikey}&url={webwithouthttp}")
    
    parsed_data = jsonrequest.json()
    print("Technologies Detected: ")
    if 'result' in parsed_data and parsed_data['result']['code'] == 200:
        for technology in parsed_data.get('results',[]):
            name = technology.get('name', 'Unknown')
            version = technology.get('version', 'N/A')
            category = technology.get('categories', 'N/A')
            print(f"Name:{name}, Version:{version}, Used As: {category}")
if __name__ == "__main__":
    main()