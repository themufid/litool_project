import requests
from utils.http import HttpUtils

class Scanner:
    def __init__(self, url, logger):
        self.url = url if url.startswith("http://") or url.startswith("https://") else "http://" + url
        self.logger = logger

    def scan(self):
        self.logger.log("Scanning for vulnerabilities...")
        response = HttpUtils.send_request(self.url)
        if response:
            vulnerabilities = self.detect_vulnerabilities(response)
            if vulnerabilities:
                self.logger.log("Vulnerabilities detected:")
                for vulnerability in vulnerabilities:
                    self.logger.log(f"- {vulnerability}")
            else:
                self.logger.log("No vulnerabilities detected.")
        else:
            self.logger.log("Failed to get a response from the target.")

    def detect_vulnerabilities(self, response):
        vulnerabilities = []
        if "SQL syntax error" in response.text:
            vulnerabilities.append("SQL Injection")
        return vulnerabilities
