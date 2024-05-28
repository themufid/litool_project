import requests

class HttpUtils:
    @staticmethod
    def send_request(url, timeout=10):
        try:
            response = requests.get(url, timeout=timeout, verify=False)
            return response
        except requests.RequestException as e:
            print(f"HTTP request failed: {e}")
            return None
