# lib/Scraper.py
from bs4 import BeautifulSoup
import requests
from Course import Course

class Scraper:
    def __init__(self):
        """Initialize the Scraper with an empty list of courses."""
        self.courses = []

    def get_page(self):
        """Fetch and parse the HTML content of the course page.

        Returns:
            BeautifulSoup object if successful, None if the request fails.
        """
        try:
            response = requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses")
            response.raise_for_status()
            doc = BeautifulSoup(response.text, 'html.parser')
            return doc
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def get_courses(self):
        """Get all course elements from the page using a CSS selector.

        Returns:
            List of BeautifulSoup elements representing courses.
        """
        doc = self.get_page()
        if doc is None:
            return []
        return doc.select('.post')

    def make_courses(self):
        """Create Course objects from the scraped data.

        Returns:
            List of Course objects.
        """
        for course in self.get_courses():
            title = course.select("h2")[0].text if course.select("h2") else ''
            schedule = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''
            new_course = Course(title, schedule, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        """Print all courses using their string representation."""
        for course in self.make_courses():
            print(course)

if __name__ == "__main__":
    scraper = Scraper()
    scraper.print_courses()