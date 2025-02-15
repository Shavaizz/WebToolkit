import requests
# No need for APIs in this request
def desktop_speed_getter(url):
    try:
        response = requests.get(f"https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed/?url=https://{url}")
        response.raise_for_status()
        parsed_data = response.json()
        overall_score = parsed_data.get("loadingExperience", {}).get("overall_category", "Realtime Data Can't be found")
        largest_contentful_paint = parsed_data.get("lighthouseResult", {}).get("audits",{}).get("largest-contentful-paint", {}).get("displayValue","Key not found")
        print(f"Overall Average Speed For Desktop: {overall_score} (Based On Realtime Data), Largest Contentful Paint: {largest_contentful_paint} (Lighthouse)")
    except Exception as e:
        print(f"Error Occured: {e}")
def mobile_speed_getter(url):
    try:
        response = requests.get(f"https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed/?strategy=MOBILE&url=https://{url}")
        response.raise_for_status()
        parsed_data = response.json()
        overall_score = parsed_data.get("loadingExperience", {}).get("overall_category", "Realtime Data Can't be found")
        largest_contentful_paint = parsed_data.get("lighthouseResult", {}).get("audits",{}).get("largest-contentful-paint", {}).get("displayValue","Key not found")
        print(f"Overall Average Speed For Mobile: {overall_score} (Based On Realtime Data), Largest Contentful Paint: {largest_contentful_paint} (Lighthouse)")
    except Exception as e:
        print(f"Error Occured: {e}")
def main():
    try:
        with open("website.txt", "r") as file:
            website_checker_url = file.read().strip()
        if not website_checker_url:
            print("Error: Website URL is missing. Please make sure the Website URL is set in your .env file.")
    except Exception as e:
        print(f"Error Occured When Making Request: {e}")
    try:
        webwithouthttp = website_checker_url
        print("Fetching Realtime and Lighthouse Speed Results")
        desktop_speed_getter(webwithouthttp)
        mobile_speed_getter(webwithouthttp)
    except ValueError:
        print("Error: Failed to parse JSON response from the API.")
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":
    main()
