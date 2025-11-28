# MOVIE_R
A Python-based IMDb Movie Scraper using Selenium
🎬 Project Overview

This project is an automated IMDb Movie Scraper built using Python, Selenium WebDriver, WebDriver Manager, and Pandas.
The script extracts details of top movies from IMDb and saves the data into a CSV file for further analysis or research.

📌 Features

Scrapes movie title, year, rating, and rank

Extracts movie links for more details

Automatically launches browser using WebDriver Manager

Stores extracted data in a Pandas DataFrame

Exports clean data directly into a CSV file

🛠️ Tech Stack

Python

Selenium WebDriver

WebDriver Manager

Pandas

Chrome / Edge WebDriver

🚀 How It Works

Selenium opens the IMDb page automatically

Script locates movie elements by XPath / CSS selectors

Extracts and stores movie details

Converts data into a DataFrame

Saves output as imdb_movies.csv

📂 Project Structure
|-- imdb_scraper.py
|-- requirements.txt
|-- imdb_movies.csv  (output)
|-- README.md

▶️ How to Run the Project
1. Install Dependencies
pip install -r requirements.txt

2. Run the Script
python imdb_scraper.py

3. Output

A CSV file named imdb_movies.csv will be created in your project folder.

📊 Sample Output
Rank	Title	Year	Rating	Link
1	The Shawshank Redemption	1994	9.2	imdb.com/...
🌟 Use Cases

Data analysis

Movie research

ML model input

Automation learning

Data collection for dashboards

💡 What I Learned

Browser automation

Web scraping techniques

Handling dynamic website elements

Data cleaning using Pandas

Exporting structured data

📎 Future Enhancements

Add genre extraction

Download posters

Scrape multiple pages

Add GUI

Store data in a database
