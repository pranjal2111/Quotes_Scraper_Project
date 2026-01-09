import requests  # For getting web pages
from bs4 import BeautifulSoup  # For reading HTML
import csv  # For saving to CSV
import sqlite3  # For saving to database
import os  # For path handling

# Ensure we're in the project root
os.chdir(os.path.dirname(__file__))  # Change to script's directory


# Function to scrape one page
def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)  # Get the page with timeout
        response.raise_for_status()  # Check for errors
        soup = BeautifulSoup(response.text, 'html.parser')  # Read the HTML
        quotes = []  # Empty list for quotes

        # Find each quote box
        for quote_div in soup.find_all('div', class_='quote'):
            text = quote_div.find('span', class_='text').get_text(strip=True)  # Get quote text
            author = quote_div.find('small', class_='author').get_text(strip=True)  # Get author
            tags = [tag.get_text() for tag in quote_div.find_all('a', class_='tag')]  # Get tags
            tags_str = ', '.join(tags)  # Join tags into one string
            author_profile = quote_div.find('a')['href']  # Get profile link

            # Add to list
            quotes.append({
                'quote': text,
                'author': author,
                'tags': tags_str,
                'author_profile': author_profile
            })

        return quotes  # Return the list
    except Exception as e:
        print(f"Error scraping: {e}")
        return []


# Main function to scrape (only one URL)
def scrape_quotes():
    all_quotes = []
    for page in range(1, 11):  # 10 pages
        url = f'https://quotes.toscrape.com/page/{page}/'
        print(f"Scraping page {page}...")
        quotes = scrape_page(url)
        all_quotes.extend(quotes)
    print(f"Total quotes scraped: {len(all_quotes)}")
    return all_quotes



# Save to CSV (easy file)
def save_to_csv(quotes):
    if not quotes:
        print("No quotes to save!")
        return
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['quote', 'author', 'tags', 'author_profile'])
        writer.writeheader()  # Add headers
        writer.writerows(quotes)  # Add rows
    print("Saved to quotes.csv")


# Save to SQLite DB (simple table)
def save_to_db(quotes):
    if not quotes:
        print("No quotes to save!")
        return
    conn = sqlite3.connect('quotes.db')  # Connect to DB
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS quotes (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT UNIQUE,
        author TEXT,
        tags TEXT,
        author_profile TEXT
    )''')  # Create table

    for quote in quotes:
        cursor.execute(
            'INSERT OR IGNORE INTO quotes (quote, author, tags, author_profile) VALUES (?, ?, ?, ?)',
            (quote['quote'], quote['author'], quote['tags'], quote['author_profile'])
        )

    conn.commit()  # Save
    conn.close()  # Close
    print("Saved to quotes.db")


# Run everything
if __name__ == '__main__':
    quotes = scrape_quotes()  # Scrape
    save_to_csv(quotes)  # Save CSV
    save_to_db(quotes)  # Save DB