from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


html_doc = '''
<html>
<head>
<title>A Useful Page</title>
</head>
<body>
<h1>An Interesting Title</h1>
<div>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>
</body>
</html>
'''
html = urlopen('https://prosettings.net/cs-go-pro-settings-gear-list/')
soup = BeautifulSoup(html)
print(soup.prettify())

# print(soup.find(text="dolor"))
# print(soup.find(text=re.compile("dolor")))
