📜 Quotes Scraper Project

A Python-based web scraping and web application project that scrapes inspirational quotes from quotes.toscrape.com, stores the data in CSV and SQLite, and displays it through a simple Django web application.

This project demonstrates skills in web scraping, data storage, backend development, and Django integration.


---

🚀 Features

Scrapes quotes from multiple pages (pagination supported)

Extracts:

Quote text

Author name

Tags

Author profile URL


Saves data into:

CSV file

SQLite database


Prevents duplicate records (optional handling)

Displays scraped data in a Django web application

Clean and readable UI



---

🛠️ Tech Stack

Programming Language: Python

Web Scraping: Requests, BeautifulSoup

Database: SQLite

Web Framework: Django

Data Storage: CSV

Frontend: HTML, CSS (basic styling)



---

📂 Project Structure

Quotes_Scraper_Project/
│
├── scraper/
│   ├── scrape_quotes.py
│   ├── quotes.csv
│   └── quotes.db
│
├── quotes_web/
│   ├── manage.py
│   ├── quotes_app/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   │       └── quotes.html
│
├── requirements.txt
└── README.md


---

📌 Scraping Details

Target Website: https://quotes.toscrape.com/

Pages Scraped: Minimum 10 pages

Scraped Fields:

quote

author

tags

author_profile




---

⚙️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/pranjal2111/Quotes_Scraper_Project.git
cd Quotes_Scraper_Project

2️⃣ Create Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt


---

🧹 Run the Scraper

python scraper/scrape_quotes.py

✔ This will:

Scrape quotes from multiple pages

Save data to quotes.csv

Store data in quotes.db (SQLite)



---

🌐 Run the Django Web Application

cd quotes_web
python manage.py migrate
python manage.py runserver

Open your browser and visit:

http://127.0.0.1:8000/

✔ You will see:

Quote text

Author name

Tags

Clickable author profile links



---

📊 Output Files

CSV File: quotes.csv

Database File: quotes.db

Web View: Django-rendered HTML page



---

🧠 Learning Outcomes

Practical experience with web scraping

Handling pagination programmatically

Working with CSV & SQLite

Django backend development

Data visualization through web UI

Writing clean, modular Python code


---

👨‍💻 Author

Pranjal Vejani
Computer Engineering Graduate 
Python & Django Developer

🔗 GitHub: pranjal2111
