from transformers import pipeline


class Model:

    def predict(self, text):
        # specificModel is getting the require model using pipeline
        specificModel = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
        # result variable getting the result using the model
        result = specificModel(text)
        # sentiment variable storing the specific label from result variable
        sentiment = result[0]['label']
        # As per requirement sentiment storing the specific string
        if sentiment == 'POS':
            sentiment = 'positive'
        elif sentiment == 'NEG':
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        return sentiment


# making a temporary model class
# that will delivered when need to use this class
model = Model()


def get_model():
    return model
