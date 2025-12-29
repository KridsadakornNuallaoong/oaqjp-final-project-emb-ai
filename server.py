"""Flask server for emotion detection API."""
from final_project.emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def detect_emotion():
    """Detect emotion from the provided text."""
    text_to_analyze = request.args.get('textToAnalyze')

    try:
        detected_emotion = emotion_detector(text_to_analyze)
    except ValueError as e:
        return f"<h2>Invalid text! Please try again!. Error: {str(e)}</h2>"

    for key in detected_emotion:
        if key != "dominant_emotion":
            detected_emotion[key] = f"{detected_emotion[key]:.9f}"

    result = (
        "For the given statement, the system response is "
        f"anger: {detected_emotion['anger']}, "
        f"disgust: {detected_emotion['disgust']}, "
        f"fear: {detected_emotion['fear']}, "
        f"joy: {detected_emotion['joy']}, "
        f"sadness: {detected_emotion['sadness']}. "
        f"The dominant emotion is {detected_emotion['dominant_emotion']}."
    )

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
