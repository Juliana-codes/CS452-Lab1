# Import the required libraries
import requests  # For making HTTP requests to retrieve the webpage
from bs4 import BeautifulSoup  # For parsing HTML content

# Send an HTTP GET request to the Millersville University homepage
response = requests.get("https://dl.acm.org/toc/jacm/current")

# Check if the request was successful (status code 200)
if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()  # Exit the program if the webpage couldn't be retrieved

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Open a file to store the extracted news titles
# The file will be created or overwritten if it already exists
output_file = open("section_titles.txt", "w")

# Initialize an empty list to store the news titles
section_titles = []

# Locate all <a> elements with the class "left-bordered-title.section__title sccordion-tabbed__control"
all_sections = soup.find_all('a', attrs={'class': 'left-bordered-title.section__title sccordion-tabbed__control'})
#print(section_titles)

# Iterate through each <a> element and extract its text
for heading in all_sections:
    title = heading.text.strip()  # Extract and clean the text inside the <a> element
    section_titles_titles.append(title)  # Add the title to the list
    print(title)  # Print the title to the console for verification

# Sort the list of news titles alphabetically
#section_titles.sort()

# Write each sorted news title to the output file
for title in section_titles:
    output_file.write(title + "\n")  # Add a newline after each title

# Close the file to ensure data is saved properly
output_file.close()

# Print a confirmation message
print(f"Section titles have been successfully written to 'section_titles.txt'.")