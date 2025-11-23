import requests
import json

def emotion_detector(text_to_analyze):
    #Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #Set the headers with the correct model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #Create the payload with the text to be analysed 
    myobj = { "raw_document": { "text": text_to_analyze } }

    #Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    #Parse the response from the API
    formatted_response = json.loads(response.text)

    #Extract the emotions 
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    
    #Identify the dominant emotion
    emotion['dominant_emotion'] = max(emotion, key=emotion.get)

    if response.status_code == 200:
        return emotion

    elif response.status_code == 400:    
        return{
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    else:
        raise Exception(f"Unexpected status code: {response.status_code}")