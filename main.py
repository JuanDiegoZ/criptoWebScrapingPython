from inspect import classify_class_attrs
from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml' )
    courses_html_tags = soup.findAll('div', class_ ='css-12ujz79')
    for course in courses_html_tags:
        print(course)