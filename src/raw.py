import os
import requests
from bs4 import BeautifulSoup
import csv
import re

# Function to clean text
def clean_text(text):
    # Remove special characters except spaces
    return re.sub(r'[^\w\s]', '', text)


# Function to scrape the FAQ page
def scrape_faq_page(url, csv_writer):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the FAQ items (adjusting the selector to match the new structure)
        faq_container = soup.find('div', class_='promotion-lists box-scoll')
        faq_items = faq_container.find_all('div', class_='item')
        
        # Extract and write the questions and answers
        for item in faq_items:
            question = item.find('a').get_text(strip=True)
            answer = item.find('div', class_='des').get_text(strip=True).replace('\u200b', '').replace('\u200b', '').replace('\u200b', '')

            # Clean the text in the DataFrame
            question = clean_text(question)
            answer = clean_text(answer)
            
            # Write to CSV
            csv_writer.writerow([question, answer])
        
        print(f"Data from {url} has been written to CSV file")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == '__main__':
    categories_file = "data/vcb/raw_info.txt"

    # Read categories and page numbers from the .txt file
    categories = []
    with open(categories_file, 'r', encoding='utf-8') as file:
        for line in file:
            name, pages = line.strip().split(',')
            categories.append((name, int(pages)))

    # Output CSV file path
    output_file = "data/vcb/faq.csv"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Remove the file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"Removed existing file: {output_file}")
    else:
        print(f"File does not exist: {output_file}")

    

    # Open the CSV file for writing
    with open(output_file, 'a', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        # Write the header row
        csv_writer.writerow(["Question", "Answer"])
        for category_name, max_pages in categories:
            # Scrape multiple pages and write data to the CSV file
            for i in range(1, max_pages):
                # URL of the FAQ page
                url = f"https://portal.vietcombank.com.vn/FAQs/Pages/{category_name}.aspx?Page={i}&devicechannel=default"
                
                # Scrape the FAQ page and write data to the CSV file
                scrape_faq_page(url, csv_writer)
