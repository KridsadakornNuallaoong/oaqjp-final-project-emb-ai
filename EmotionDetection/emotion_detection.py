import json

import requests
import os

def emotion_detector(text_to_analyze):
    URL = 'http://' + os.getenv("API_URI") + '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    Input_json = { "raw_document": { "text": text_to_analyze } }

    # TODO: Make the POST request to the Watson NLP service and handle errors
    try:
        response = requests.post(URL, headers=Headers, data=json.dumps(Input_json))
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
        response.raise_for_status()

        # TODO: Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores.
        response = response.json()
        response_json = {
            "anger": response["anger"],
            "disgust": response["disgust"],
            "fear": response["fear"],
            "joy": response["joy"],
            "sadness": response["sadness"],
            "dominant_emotion": response["dominant_emotion"]
        }
        return response_json
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error during request to NLP service: {e}")
