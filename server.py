"""
This module sets up a Flask web application for emotion detection.
It includes routes for rendering the index page and processing emotion analysis requests.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

# Initialize the Flask application
app = Flask("Sentiment Analyzer")

@app.route('/')
def index():
    """
    Render the index.html template for the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Retrieve the input text from the user, process it using the emotion detector, 
    and return a formatted string with the emotion analysis results.
    
    Returns:
        str: The formatted string with the emotion analysis results or an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function and get the result
    result = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None (indicating an error)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format the result for display
    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    # Run the Flask application on the specified host and port.
    app.run(host="0.0.0.0", port=5000)
