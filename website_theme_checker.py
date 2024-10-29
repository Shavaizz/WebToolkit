import requests
from dotenv import load_dotenv
import os
load_dotenv()

apikey = os.environ['apikey']
def main():
    try:
        with open("website.txt", "r") as file:
            website_checker_url = file.read().strip()
    except FileNotFoundError:
        print("No website URL found. Please run the first script.")
    
    webwithouthttp = website_checker_url
    jsonrequest = requests.get(f"https://www.themedetect.com/API/Theme?url={webwithouthttp}&key={apikey}")
    parsed_data = jsonrequest.json()
    if 'result' in parsed_data and parsed_data['result']['code']==200:
        for technology in parsed_data.get('results',[]):
            name = technology.get('theme_name','Unkown')
            license  = technology.get('license', 'Unkown')
            print(f"Name: {name}, Version: {license}")
if __name__ == "__main__":
    main()