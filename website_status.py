import requests
import dotenv
def main():
    website_url = input("What website are you checking?: ").strip()
    webwithouthttp = f"https://www.{website_url}"
    if   website_url == "":
        print("Empty strings aren't allowed try again")
    else:
        webwithouthttp = f"https://www.{website_url}"
        with open("website.txt", "w") as file:
            file.write(website_url)

    statuses = {
        200: "Website Available",
        301: "Permanent Redirect",
        302: "Temporary Redirect",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable"
    }
    def website_status_checker(web):
        try:
            web_response = requests.get(web)
            print(f"{statuses[web_response.status_code]}, Code:{web_response.status_code}")
        except:
            if statuses[web_response.status_code] == 200:
                print(statuses[web_response.status_code])
            else:
                print("Website doesn't work / unavailable")   
    website_status_checker(webwithouthttp)
    
if __name__ == "main":
    main()