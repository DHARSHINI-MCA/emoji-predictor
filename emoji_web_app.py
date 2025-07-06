import gradio as gr
import joblib

# Load model and vectorizer
model = joblib.load('emoji_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Prediction function
def predict_emoji(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return f"Predicted emoji: {prediction}"

# Gradio interface
interface = gr.Interface(
    fn=predict_emoji,
    inputs=gr.Textbox(lines=2, placeholder="Enter your text here..."),
    outputs="text",
    title="Emoji Predictor 😊",
    description="Enter any text, and see which emoji your ML model predicts!"
)

# Launch app
interface.launch(share=True)

