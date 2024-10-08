''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """ Route for call to Emotion Detector """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Check if the label is None, indicating an error or invalid input
    if (response["anger"]) == 'None':
        return "Invalid input! Try again."
    # Else return a formatted string with the emotion detection scores
    return response

@app.route("/")
def render_index_page():
    """ Route for call to the Index page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
