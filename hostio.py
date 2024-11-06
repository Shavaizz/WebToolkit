import requests
from dotenv import load_dotenv
import os
load_dotenv()


apikeyhostio= os.environ['hostio_key']

def main():
    try:
        with open("website.txt", "r") as file:
            website_checker_url = file.read().strip()
    except FileNotFoundError:
        print("No website URL found. Please run the first script.")
    website = website_checker_url
    try:

        jsonrequests = requests.get(f"https://host.io/api/related/{website}?token={apikeyhostio}")
        jsonrequests.raise_for_status()  
        
        jsondata = jsonrequests.json()
        
        if "email" in jsondata:
            print("\nEmails:")
            for email in jsondata["email"]:
                print(f"  - {email['value']} (count: {email['count']})")

        if "ns" in jsondata:
            print("\nNameservers (NS):")
            for ns in jsondata["ns"]:
                print(f"  - {ns['value']}")
        
        if "ip" in jsondata:
            print("\nIP Addresses:")
            for ip in jsondata["ip"]:
                print(f"  - {ip['value']} (count: {ip['count']})")
        
        if "backlinks" in jsondata:
            print("\nBacklinks:")
            for backlink in jsondata["backlinks"]:
                print(f"  - {backlink['value']} (count: {backlink['count']})")
        
        if "redirects" in jsondata:
            print("\nRedirects:")
            for redirect in jsondata["redirects"]:
                print(f"  - {redirect['value']} (count: {redirect['count']})")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
    
    
    