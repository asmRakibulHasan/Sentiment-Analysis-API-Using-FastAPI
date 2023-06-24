# Sentiment-Analysis-API-Using-FastAPI

Deploy a pre-trained BERT model for Sentiment Analysis as a REST API using FastAPI

## Demo

The model is trained to classify sentiment (negative, neutral, and positive). Here's a sample request to the API:

```bash
http POST http://127.0.0.1:8000/predict text="Good basic lists, i would like to create more lists, but the annual fee for unlimited lists is too out there"
```

The response you'll get looks something like this:

```js
{
    "sentiment": "neutral"
}
```
## Installation

Clone this repo:

```sh
git@github.com:asmRakibulHasan/Sentiment-Analysis-API-Using-FastAPI.git
cd Sentiment-Analysis-API-Using-FastAPI
```

Install the dependencies:

```sh
pip3 install fastapi uvicorn torch transformers pydantic
```


## Test the setup

Start the HTTP server:

```sh
bin/start_server
```

Send a test request:

```sh
bin/test_request
```
