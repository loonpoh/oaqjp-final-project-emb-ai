""" imports                         """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotiondetector():
    """       Emotion Detector                         """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid input! Try again."
    emotion_details = (
    f"'anger': {response['anger']:.6f}, "
    f"'disgust': {response['disgust']:.6f}, "
    f"'fear': {response['fear']:.6f}, "
    f"'joy': {response['joy']:.6f} and "
    f"'sadness': {response['sadness']:.6f}"
)
    response_str = "For the given statement, the system response is" + emotion_details + "."  \
    "The dominant emotion is " + ":" + response["dominant_emotion"]
    # Return a formatted string with the sentiment label and score
    return response_str

@app.route("/")
def render_index_page():
    """ render page                """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5090)
