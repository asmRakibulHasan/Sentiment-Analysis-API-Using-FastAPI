# Sentiment-Analysis-API-Using-FastAPI

Deploy a pre-trained model for Sentiment Analysis as a REST API using FastAPI

## Demo

The model is trained to classify sentiment (negative, neutral, and positive). Here's a sample request to the API:

The response you'll get looks something like this:

```js
{
    "sentiment": "neutral"
}
```
## Installation

Clone this repo:

```sh
git clone git@github.com:asmRakibulHasan/Sentiment-Analysis-API-Using-FastAPI.git
cd Sentiment-Analysis-API-Using-FastAPI
```

Install the dependencies:

```sh
pip3 install fastapi uvicorn torch transformers pydantic
```


## Test the setup

Start the HTTP server:

```sh
uvicorn SentimentAnalysisApi.api:app --reload
```

Send a test request:

run this on browser

```sh
http://127.0.0.1:8000/docs#/default/analyze_sentiment_analyze_post
```

## Here is the example

```sh
Click on the "try it out"
```
<img src="https://raw.githubusercontent.com/curiousily/Deep-Learning-For-Hackers/master/.github/book-cover.png" width="250">

