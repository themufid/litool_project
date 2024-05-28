# Almufid Official License
# Copyright (c) 2024 Almufid Official
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# You are not allowed to use the name "Almufid Official" or any other copyright holder names for the purpose of promotion or endorsement without prior written permission.
# 
# You must include a reference to Almufid Official in all materials published or presented that use this software.

import argparse
import sys
from core.scanner import Scanner
from core.injector import Injector
from utils.logger import Logger

sys.stdout.reconfigure(encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description="litool - SQL Injection Tool")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--scan", help="Scan for SQL Injection", action="store_true")
    parser.add_argument("--inject", help="Perform SQL Injection", action="store_true")
    args = parser.parse_args()

    logger = Logger()

    if args.scan:
        scanner = Scanner(args.url, logger)
        scanner.scan()

    if args.inject:
        injector = Injector(args.url, logger)
        injector.inject()

if __name__ == "__main__":
    main()
