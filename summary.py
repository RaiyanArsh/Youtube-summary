import os
from ytgpt import youtube_video_url_is_valid, find_insights
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('summ.html')

@app.route('/summary', methods=['POST'])
def summary():
    ytUrl = request.form.get('ytUrl')
    openai_api_key = "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"
    
    youtube_video_url = ytUrl

    if not youtube_video_url_is_valid(youtube_video_url):
        return render_template('summ.html', error="Please enter a valid YouTube video URL")
    os.environ["OPENAI_API_KEY"] = "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"
    summary = find_insights(openai_api_key, youtube_video_url)
    return render_template('summ.html', summary=summary)
if __name__ == '__main__':
    app.run()