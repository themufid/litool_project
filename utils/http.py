import requests

class HttpUtils:
    @staticmethod
    def send_request(url):
        try:
            response = requests.get(url)
            return response
        except requests.RequestException as e:
            print(f"Error sending request to {url}: {e}")
            return None
