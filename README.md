# Ignition-Scraper
A Web Scraping Program has been designed specifically for Inductive University's Ignition Training, addressing the requirement of answering questions correctly, failing which one must redo the test with a mix of previously attempted and novel questions. The program effectively scrapes the questions and corresponding answers, thereby saving them in a structured table for future reference.

Required Python Libraries:
Selenium, BeautifulSoup, HTMLParser, tkinter

into command prompt.
pip install "Library Name" 

1: To initiate the program, kindly download the files and store them in a designated folder.

2: Open the IgnitionScraper.py file to proceed further.

3: Within this file, you will find the option to set your Inductive University account's Username and Password, a significant convenience as it saves you the hassle of logging in repeatedly while developing the application.

4: Additionally, you will notice the TestUrl variable, which enables you to enter the URL of your current test, automatically redirecting you to the relevant page. This feature has been thoughtfully implemented to simplify the testing process.

5: Once the program commences, it will automatically launch an instance of Firefox and display a graphical user interface (GUI) with the necessary controls.

6: Navigate to the test page, answer the questions, and when ready to record your responses, click on the "GetWebPage" button.

7: The program will save the recorded questions and corresponding answers in a table format, accessible for future reference.

Potential Issue: You may get an error about 'geckodriver' executable needs to be in PATH. This indicates you need to add the firefox/geckodriver to the system path variables for the program to function.

