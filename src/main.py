import requests
from bs4 import BeautifulSoup
import random
import time

class AntiScrapingSpider:
    def __init__(self, base_url, proxies=None):
        self.base_url = base_url
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
        ]
        self.proxies = proxies if proxies else [
            # 在此添加代理 IP 地址
            # {'http': 'http://your.proxy.ip:port', 'https': 'https://your.proxy.ip:port'}
        ]
        
    def get_random_headers(self):
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept-Language': 'en-US,en;q=0.5'
        }
        return headers

    def get_random_proxy(self):
        return random.choice(self.proxies) if self.proxies else None

    def fetch_page(self, url):
        for attempt in range(5):  # 最多重试 5 次
            try:
                headers = self.get_random_headers()
                proxy = self.get_random_proxy()
                response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
                response.raise_for_status()
                
                # 添加随机延迟
                time.sleep(random.uniform(1, 3))
                
                return response.text
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt + 1}: Error fetching {url}: {e}")
                time.sleep(random.uniform(2, 5))  # 增加重试前的等待时间
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
    spider = AntiScrapingSpider("https://example.com")
    spider.run()
