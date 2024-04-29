Ignition-Scraper
Description:
A Web Scraping Program has been designed specifically for Inductive University's Ignition Training, addressing the requirement of answering questions correctly. Failing to do so will prompt the user to redo the test with a mix of previously attempted and novel questions. The program effectively scrapes the questions and corresponding answers, thereby saving them in a structured table for future reference.

Required Python Libraries:

Selenium
BeautifulSoup
HTMLParser
tkinter
To install these libraries, run the following commands in your command prompt:

Copy code
pip install selenium
pip install beautifulsoup4
pip install html5lib
pip install tk
Instructions:

To initiate the program, kindly download the files and store them in a designated folder.
Open the IgnitionScraper.py file to proceed further.
Within this file, you will find the option to set your Inductive University account's Username and Password, a significant convenience as it saves you the hassle of logging in repeatedly while developing the application.
Additionally, you will notice the TestUrl variable, which enables you to enter the URL of your current test, automatically redirecting you to the relevant page. This feature has been thoughtfully implemented to simplify the testing process.
Once the program commences, it will automatically launch an instance of Firefox and display a graphical user interface (GUI) with the necessary controls.
Navigate to the test page, answer the questions, and when ready to record your responses, click on the "GetWebPage" button.
The program will save the recorded questions and corresponding answers in a table format, accessible for future reference.
Potential Issue:
You may encounter an error stating that the 'geckodriver' executable needs to be in PATH. This indicates you need to add the Firefox/geckodriver directory to the system path variables for the program to function properly.

