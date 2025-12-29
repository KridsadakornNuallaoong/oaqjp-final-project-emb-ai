import unittest

from EmotionDetection.emotion_detection import emotion_detector


def print_test_result(texttoanalyze, expected_emotion, detected_emotion):
    print(f"Test Text: {texttoanalyze}")
    print(f"Expected Dominant Emotion: {expected_emotion}")
    print(f"Detected Dominant Emotion: {detected_emotion}")
    print("Test Passed!" if expected_emotion == detected_emotion else "Test Failed!")
    print("-" * 50)

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        print_test_result(text, "joy", result["dominant_emotion"])
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        print_test_result(text, "anger", result["dominant_emotion"])
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        print_test_result(text, "disgust", result["dominant_emotion"])
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        print_test_result(text, "sadness", result["dominant_emotion"])
        self.assertEqual(result["dominant_emotion"], "sadness")
        
    def test_fear(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        print_test_result(text, "fear", result["dominant_emotion"])
        self.assertEqual(result["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()