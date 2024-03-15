# Website Content Summerizer Api
The goal of this project is to create an API that can scrape through a websit and output the a summary of the contents on the website.
I published it directly from visual studio code.

# STEP 1
After running the code in the file main.py the terminal will run the ask you for a prompt, enter them one at a time in chronological order;
1. cd summarize
2. uvicorn --host 0.0.0.0 "main:app"

# STEP 2
After entering the code above you will see the server begin to run, paste the following URL's each in it's own tab.

#http://localhost:8000

#http://localhost:8000/docs

# STEP 3
After running the last API you will be taken to FastAPI, from where you can use the find the code url: str .
Replace the str with any url you want, make sure to include "".

Example
url:"https://en.wikipedia.org/wiki/Microsoft_Azure"

This will show you the contents of Microsoft Azure on the Wikipedia webpage.
