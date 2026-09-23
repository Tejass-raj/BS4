# 📰 Hacker News Web Scraper

A simple Python web scraping project built using **Requests** and **BeautifulSoup**.

The project sends a request to Hacker News, reads the HTML response, and uses BeautifulSoup to find the first article on the page. It then extracts and prints the article title and link.

I also included a basic HTML file to practice working with BeautifulSoup on locally stored HTML pages.

## 📖 Overview

The main goal of this project is to understand the basics of **web scraping in Python**.

The Python script:

1. Sends a GET request to Hacker News.
2. Gets the HTML content of the webpage.
3. Parses the HTML using BeautifulSoup.
4. Finds the first article title.
5. Extracts the article text.
6. Extracts the article link.
7. Prints the results in the terminal.

The project uses the Hacker News website as the example source. The request and HTML parsing are handled using `requests` and `BeautifulSoup`. 

## ✨ Features

- Fetches webpage content using Python
- Parses HTML using BeautifulSoup
- Finds HTML elements using tags and classes
- Extracts article title
- Extracts article URL
- Prints scraped data in the terminal
- Includes a sample HTML file for local parsing practice

## 🛠️ Technologies Used

- **Python**
- **Requests**
- **BeautifulSoup4**
- **HTML**

## 📂 Project Structure

```text
Hacker-News-Scraper/
│
├── main.py
├── website.html
└── README.md
