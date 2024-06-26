import requests
from utils.http import HttpUtils

class Scanner:
    def __init__(self, url, logger):
        self.url = url if url.startswith("http://") or url.startswith("https://") else "http://" + url
        self.logger = logger
        self.timeout = 10

    def set_timeout(self, timeout):
        self.timeout = timeout

    def scan(self):
        self.logger.log("Scanning for vulnerabilities...")
        response = HttpUtils.send_request(self.url, self.timeout)
        results = []
        if response:
            if "internetpositif.id" in response.url:
                self.logger.log("This website is potentially dangerous.")
                results.append("This website is potentially dangerous.")
            else:
                self.logger.log(f"Received response: {response.status_code} {response.reason}")
                if response.status_code == 200:
                    self.logger.log("This website is safe.")
                    results.append("This website is safe.")
                else:
                    self.logger.log("This website may be unsafe.")
                    results.append("This website may be unsafe.")
                vulnerabilities = self.detect_vulnerabilities(response)
                if vulnerabilities:
                    self.logger.log("Vulnerabilities detected:")
                    for vulnerability in vulnerabilities:
                        self.logger.log(f"- {vulnerability}")
                    results.append("Vulnerabilities detected")
                else:
                    self.logger.log("No vulnerabilities detected.")
                    results.append("No vulnerabilities detected")
        else:
            self.logger.log("Failed to get a response from the target.")
            results.append("Failed to get a response")
        return results

    def detect_vulnerabilities(self, response):
        vulnerabilities = []
        if "SQL syntax error" in response.text:
            vulnerabilities.append("SQL Injection")
        return vulnerabilities
