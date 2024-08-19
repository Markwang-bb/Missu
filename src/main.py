import requests
from bs4 import BeautifulSoup

class SimpleSpider:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers if headers else {'User-Agent': 'Mozilla/5.0'}
        
    def fetch_page(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_html(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

    def extract_data(self, soup):
        # 在这里根据具体网页结构提取所需数据
        data = {}
        data['title'] = soup.title.string if soup.title else "No Title"
        # 添加更多提取逻辑
        return data

    def run(self):
        html_content = self.fetch_page(self.base_url)
        if html_content:
            soup = self.parse_html(html_content)
            data = self.extract_data(soup)
            print(data)
        else:
            print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    spider = SimpleSpider("https://example.com")
    spider.run()
