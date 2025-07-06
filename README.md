# emoji-predictor
# 🧠 Simple Emoji Predictor (ML Mini Project)

A mini machine learning project I created to learn text classification!  
It predicts an emoji for your text based on what you type.

## ✅ Supported Emojis:
| Emoji | Meaning               |
|------|-----------------------|
| 😊    | happy / positive      |
| 😢    | sad / depressed      |
| 😂    | funny / laugh        |
| 😡    | angry / frustration  |
| 🤩    | excited / amazed     |
| 😴    | sleepy / tired       |
| ❤️    | love / caring        |
| 💔    | broken / hurt        |
| 😱    | scared / afraid      |
| 😋    | hungry               |

> ⚠ Note: The model can only predict these 10 emojis.  
> Texts that don’t match them may get an unexpected prediction.

## 📦 How it works
- Collected ~20 sample texts for each emoji
- Used `TfidfVectorizer` + `LogisticRegression` for single-label classification
- Trained and saved model as `emoji_model.pkl`
- Simple web app built with Gradio (`emoji_web_app.py`)

## 🌱 Why I built this
To practice:
- Text preprocessing
- Training & saving a ML model
- Creating a tiny web app

## 🚀 How to run
```bash
pip install gradio joblib
pip install scikit-learn
python emoji_web_app.py
