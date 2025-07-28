# scraper.py
import requests
from bs4 import BeautifulSoup
from readability import Document

def scrape_website(url, tag='p', class_name=None):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        
        if class_name:
            elements = soup.find_all(tag, class_=class_name)
        else:
            elements = soup.find_all(tag)
        
        results = [el.get_text(strip=True) for el in elements]
        return results[:10]  # Limit to 10 results to avoid overload
    except Exception as e:
        return [f"Error: {str(e)}"]

def auto_scrape(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        doc = Document(response.text)
        summary_html = doc.summary()
        soup = BeautifulSoup(summary_html, 'html.parser')
        return soup.get_text(separator="\n", strip=True).split("\n")[:10]  # Limit to top 10 lines
    except Exception as e:
        return [f"[Auto-Scrape Error] {str(e)}"]

def scrape_youtube_titles(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = [tag.text for tag in soup.find_all("a") if "watch" in tag.get("href", "")]
        return list(set(titles))[:10]
    except Exception as e:
        return [f"Error scraping YouTube: {str(e)}"]

def scrape_twitter(username):
    try:
        url = f"https://nitter.net/{username}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tweets = [tag.text for tag in soup.find_all("div", class_="tweet-content")]
        return tweets[:5] if tweets else ["Unable to fetch tweets. Try again later."]
    except Exception as e:
        return [f"Error scraping Twitter: {str(e)}"]

def scrape_amazon_title(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find("span", id="productTitle")
        return [title.get_text(strip=True)] if title else ["Amazon product title not found."]
    except Exception as e:
        return [f"Error scraping Amazon: {str(e)}"]

def smart_scrape(url):
    if "youtube.com" in url:
        return scrape_youtube_titles(url)
    elif "amazon." in url:
        return scrape_amazon_title(url)
    elif "twitter.com" in url:
        username = url.split("/")[-1]
        return scrape_twitter(username)
    else:
        return auto_scrape(url)
