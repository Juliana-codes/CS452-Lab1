import requests
from bs4 import BeautifulSoup

#send http GET request to the acm homepage
response = requests.get("https://dl.acm.org/toc/jacm/current")

# check if the request was successful
if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    ()  # Exit the program if the webpage couldn't be retrieved

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')


# Locate all <a> tags that have the class "left-bordered-title.section__title sccordion-tabbed__control"
finding_sections = soup.find_all('div', attrs={'class': 'toc__section accordion_tabbed__tab js--open'})
sections = finding_sections.find_all('a', attrs={'class': 'left-bordered-title.section__title sccordion-tabbed__control'})

# Check if the list is not empty before accessing elements
if len(sections) > 1:
    print(sections[0])  # Print the second <a> element with the specified class
    print(sections[0].text)  # Print the text inside the second <a> element
else:
    print("No <a> elements found with the specified class.")


