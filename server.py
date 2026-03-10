"""
Executing this initiates the Flask application of 
emotion detection on localhost:5000
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Root Route. Loads the Form for inputting text to load
    """

    return render_template("index.html")

@app.route('/emotionDetector')
def emotion_detect():
    """
    Receives textToAnalyze. Runs emotion analysis.
    Returns output as humanized string.
    """

    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == '__main__':
    app.run(port=5000, debug=True)
