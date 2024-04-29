# Ignition-Scraper

## Description
A Web Scraping Program designed specifically for Inductive University's Ignition Training. It addresses the requirement of answering questions correctly, failing which one must redo the test with a mix of previously attempted and novel questions. The program effectively scrapes the questions and corresponding answers, saving them in a structured table for future reference.

## Required Python Libraries
- Selenium
- BeautifulSoup
- HTMLParser
- tkinter

```bash
pip install selenium
pip install beautifulsoup4
pip install html5lib
pip install tk
```

## Instructions
1. To initiate the program, kindly download the files and store them in a designated folder.
2. Open the `IgnitionScraper.py` file to proceed further.
3. Within this file, you will find the option to set your Inductive University account's Username and Password, a significant convenience as it saves you the hassle of logging in repeatedly while developing the application.
4. Additionally, you will notice the `TestUrl` variable, which enables you to enter the URL of your current test, automatically redirecting you to the relevant page. This feature has been thoughtfully implemented to simplify the testing process.
5. Once the program commences, it will automatically launch an instance of Firefox and display a graphical user interface (GUI) with the necessary controls.
6. Navigate to the test page, answer the questions, and when ready to record your responses, click on the "GetWebPage" button.
7. The program will save the recorded questions and corresponding answers in a table format, accessible for future reference.

## Potential Issue
You may encounter an error stating that the 'geckodriver' executable needs to be in PATH. This indicates you need to add the Firefox/geckodriver directory to the system path variables for the program to function properly.
