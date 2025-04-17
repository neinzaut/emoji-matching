from flask import Flask, render_template, request
import emoji
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

def get_emoji(sentiment_score):
    if sentiment_score >= 0.5: 
        return emoji.emojize(":grinning_face_with_smiling_eyes:")  # :D     
    elif sentiment_score > 0 and sentiment_score < 0.5: 
        return emoji.emojize(":slightly_smiling_face:")  # :)   
    elif sentiment_score == 0: 
        return emoji.emojize(":neutral_face:")  # :|       
    elif sentiment_score > -0.5: 
        return emoji.emojize(":slightly_frowning_face:")  #  :(      
    else: 
        return emoji.emojize(":angry_face:")  # >:(

@app.route('/', methods=['GET', 'POST'])
def analyze():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        sentiment = sia.polarity_scores(text)
        sentiment_score = sentiment['compound']
        matched_emoji = get_emoji(sentiment_score)
        result = f"{text} {matched_emoji}"
    return render_template('/index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
