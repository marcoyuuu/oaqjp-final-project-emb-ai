import requests  # Import the requests library to handle HTTP requests
import json  # Import the json library to handle JSON data

def emotion_detector(text_to_analyze):
    # URL of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required for the API request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Check for blank input
    if not text_to_analyze.strip():
        # Return None values if input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # The data to send in the request, including the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Check if the response status code indicates a client error (e.g., 400 Bad Request)
    if response.status_code == 400:
        # Return None values if the server returns a 400 error
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parse the response text to a dictionary
    response_dict = json.loads(response.text)
    
    # Extract the relevant emotions and their scores
    emotions = response_dict['emotionPredictions'][0]['emotion']
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Determine the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
