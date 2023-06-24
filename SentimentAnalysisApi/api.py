from fastapi import FastAPI, HTTPException
from Classifier.DataClass import AnalyzeRequest
from Classifier.model import get_model

app = FastAPI()


@app.post("/analyze")
async def analyze_sentiment(request: AnalyzeRequest):
    try:
        model = get_model()
        # Perform sentiment analysis using ML model
        sentiment = model.predict(request.text)
        # Return the result as a JSON response
        return {"sentiment": sentiment}
    except Exception as e:
        # Handle any errors and providing appropriate error responses
        raise HTTPException(status_code=500, detail=str(e))
