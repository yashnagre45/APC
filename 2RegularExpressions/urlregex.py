import re

url = input("Enter URL: ")

pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'

if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")