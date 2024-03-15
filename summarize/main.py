from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup
from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel

app = FastAPI()

class SummarizeRequest(BaseModel):
    url: str

def extract_from_url(url):
    try:
        req = urllib.request.Request(
            url, data=None,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch URL: {e}")

    parser = BeautifulSoup(html, 'html.parser')
    paragraphs = parser.find_all("p")
    if not paragraphs:
        raise HTTPException(status_code=400, detail="No <p> tags found in the HTML content.")
    
    return ' '.join(p.text.strip() for p in paragraphs)

def summarize_text(text):
    try:
        summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
        result = summarizer(text, min_length=180)
        return result[0]["summary_text"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to summarize text: {e}")

@app.post("/summarize")
def summarize(request: SummarizeRequest):
    url = request.url
    text = extract_from_url(url)
    summary = summarize_text(text)
    return {"summary": summary}

@app.get("/")
def root():
    return {"message": "Welcome to the Summarize API"}
