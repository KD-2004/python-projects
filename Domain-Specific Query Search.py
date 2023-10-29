import webbrowser
import requests
from bs4 import BeautifulSoup

def fetch_results_ddg(query):
    url = f"https://duckduckgo.com/html/?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.text

def extract_search_results_ddg(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for result in soup.select(".result__url"):
        text = result.get_text()
        href = result.get("href")
        if text and href:
            results.append({
                "text": text,
                "href": href
            })
    return results

def search_website(query, url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        # Search website name and headings for the query
        website_name = soup.find("title")
        headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

        if website_name and query in website_name.text:
            return True
        for heading in headings:
            if query in heading.text:
                return True
    except Exception as e:
        print(f"Failed to search website {url}: {e}")
    return False

def main():
    query = input("Enter your search query: ")
    ddg_html = fetch_results_ddg(query)
    ddg_results = extract_search_results_ddg(ddg_html)
    filtered_results = [result for result in ddg_results if "http" in result["href"]]

    for result in filtered_results:
        print("Text:", result["text"])
        print("URL:", result["href"])
        found = search_website(query, result["href"])
        if found:
            print("Query found on this website.")
        print("\n")

        # Open the web browser for each result
        webbrowser.open(result["href"])

if __name__ == "__main__":
    main()
