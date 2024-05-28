import requests
from utils.http import HttpUtils

class Scanner:
    def __init__(self, url, logger):
        self.url = url if url.startswith("http://") or url.startswith("https://") else "http://" + url
        self.logger = logger

    def scan(self):
        self.logger.log("Scanning for SQL Injection...")
        payloads = ["' OR '1'='1", "' OR '1'='1' --"]
        for payload in payloads:
            full_url = f"{self.url}?id={payload}"
            self.logger.log(f"Testing URL: {full_url}")
            response = HttpUtils.send_request(full_url)
            if response:
                self.logger.log(f"Response received: {response.text[:100]}...")  # Log only first 100 characters for brevity
                if "syntax" in response.text.lower() or "mysql" in response.text.lower():
                    self.logger.log(f"Possible SQL Injection found with payload: {payload}")
                else:
                    self.logger.log(f"No SQL Injection found with payload: {payload}")
            else:
                self.logger.log(f"Failed to get a response for payload: {payload}")
