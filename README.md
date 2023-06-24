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

Click on the "try it out":
![temp1](https://github.com/asmRakibulHasan/Sentiment-Analysis-API-Using-FastAPI/assets/74839882/11fb2f0e-f339-4241-bc80-69f23e6a8dde)


Then input your require String for prediction and click on "Execute":
![temp2](https://github.com/asmRakibulHasan/Sentiment-Analysis-API-Using-FastAPI/assets/74839882/acb6456c-9a93-4c5c-8ebb-cd846fbc6d29)

Here is your prediction:
![temp3](https://github.com/asmRakibulHasan/Sentiment-Analysis-API-Using-FastAPI/assets/74839882/51a3903b-d629-40f9-b5ed-fc736991550f)

