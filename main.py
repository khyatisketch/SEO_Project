# main.py

def analyze_page_content(page_content):
    # Add your SEO analysis logic here
    keyword = "SEO"
    keyword_count = page_content.lower().count(keyword.lower())
    total_words = len(page_content.split())
    keyword_density = (keyword_count / total_words) * 100

    return keyword_density


if __name__ == "__main__":
    # Fetch webpage content (you can use libraries like requests or BeautifulSoup)
    webpage_content = "<html><body><h1>Hello, World! This is an SEO tutorial.</h1></body></html>"

    # Analyze webpage content
    seo_score = analyze_page_content(webpage_content)

    # Print SEO score
    print("Keyword Density:", seo_score)
