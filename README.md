# selenium-scraper
A simple scraper using selenium and python to download lecture videos from the Brandeis Latte website. 
## Issue
The Brandeis Latte website for COSI-103 has seperate links to each lecture videos, and each link redirects the user to the zoom website, only then will the user be able to download the lecture video. This makes it difficult to download all the videos at once.
## Solution
This scraper uses selenium to automate clicking and redirecting to download all the lecture videos at once. It also collects the lecture titles and rename the downloaded videos accordingly.