import requests

website_url = input("What website are you checking?")
website_urlcleaned = website_url.strip("")
webwithouthttp = f"https://www.{website_urlcleaned}"
if website_url == "":
    print("Empty strings aren't allowed again")
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
        print(statuses[web_response.status_code])
    except:
        print(statuses[web_response.status_code])
website_status_checker(webwithouthttp)