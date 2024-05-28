import requests
from utils.http import HttpUtils

class Injector:
    def __init__(self, url, logger):
        self.url = url if url.startswith("http://") or url.startswith("https://") else "http://" + url
        self.logger = logger

    def inject(self):
        self.logger.log("Performing automatic exploitation...")
        response = HttpUtils.send_request(self.url)
        if response:
            if "SQL syntax error" in response.text:
                self.exploit_sql_injection()
            else:
                self.logger.log("No known vulnerability detected.")
        else:
            self.logger.log("Failed to get a response from the target.")

    def exploit_sql_injection(self):
        self.logger.log("SQL Injection detected, performing exploitation...")
