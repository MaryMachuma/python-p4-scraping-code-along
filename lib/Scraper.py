# lib/Scraper.py
from bs4 import BeautifulSoup
import requests
from Course import Course  # Correct import as per the lab

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        # Fetch the HTML content and parse it with Beautiful Soup
        doc = BeautifulSoup(
            requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses").text,
            'html.parser'
        )
        return doc

    def get_courses(self):
        # Use the CSS selector '.post' to get all course elements
        return self.get_page().select('.post')

    def make_courses(self):
        # Iterate over the course elements and create Course objects
        for course in self.get_courses():
            # Extract title, schedule, and description with safety checks
            title = course.select("h2")[0].text if course.select("h2") else ''
            schedule = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''

            # Create a new Course object and append it to self.courses
            new_course = Course(title, schedule, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        # Provided method to print all courses
        for course in self.make_courses():
            print(course)

# For testing purposes, you can run the scraper
if __name__ == "__main__":
    scraper = Scraper()
    scraper.print_courses()