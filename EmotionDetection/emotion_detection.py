import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = Myobj, headers=Headers)  # Send a POST request to the API with the text and headers
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    if  response.status_code == 200:
        emotionPredictions = formatted_response["emotionPredictions"][0]['emotion']
        max_label = max(emotionPredictions, key=emotionPredictions.get)  
        max_score = emotionPredictions[max_label]
        emotionPredictions["dominant_emotion"] = max_label
    elif response.status_code == 400:
        emotionPredictions = {'anger':None,"joy":None,"sadness":None,"disgust":None,"fear":None, \
        "dominant_emotion":None}
    # return {'label': max_label, 'score': max_score}
    return emotionPredictions
    