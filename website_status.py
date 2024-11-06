import requests
#No need for dotenv
def main():
    website_url = input("What domain are you checking?: ").strip()
    if website_url == "":
        print("Error: Empty strings aren't allowed. Please try again.")
        return  

    webwithouthttp = f"https://www.{website_url}"

    try:
        with open("website.txt", "w") as file:
            file.write(website_url)
        print(f"Website URL saved to 'website.txt': {website_url}")
    except Exception as e:
        print(f"Error saving the URL to 'website.txt': {e}")
        return  

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
            web_response = requests.get(web, timeout=10)  
            status_code = web_response.status_code

            if status_code in statuses:
                print(f"{statuses[status_code]}, Code: {status_code}")
            else:
                print(f"Unexpected status code: {status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to reach the website. Details: {e}")

    website_status_checker(webwithouthttp)
if __name__ == "main":
    main()