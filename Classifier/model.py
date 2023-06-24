from transformers import pipeline


class Model:

    def predict(self, text):
        specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
        result = specific_model(text)
        sentiment = result[0]['label']
        if sentiment == 'POS':
            sentiment = 'positive'
        elif sentiment == 'NEG':
            sentiment = 'negetive'
        else:
            sentiment = 'neutral'
        return sentiment


model = Model()
print(model.predict("tit for tat"))


def get_model():
    return model