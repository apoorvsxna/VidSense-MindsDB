from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    query_params = parse_qs(parsed_url.query)
    video_id = query_params.get('v', [])[0] if 'v' in query_params else None
    return video_id

def get_video_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Concatenate the text of each item in the transcript with a space
        transcript_text = ' '.join(item['text'] for item in transcript)
        return transcript_text
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

@app.route("/captions")
def get_video_transcript_route():
    youtube_url = request.args.get('youtube_url', '')
    video_id = extract_video_id(youtube_url)

    if video_id:
        transcript_text = get_video_transcript(video_id)
        transcript_text = transcript_text.replace('\n',' ')
        transcript_text = transcript_text.replace('\"', '')
        return {"t": transcript_text.replace('\n',' ')}
    else:
        return "Invalid YouTube URL"

@app.route("/summary")
def summarize():
    text = request.args.get('text', '')
    if not text:
        return jsonify({"error": "The 'text' parameter is required"}), 400

    # connect
    url = 'http://127.0.0.1:47334/api/sql/query'

    # query
    query = f'''
    SELECT * FROM google_gemini_model WHERE question = "Summarize the following: {text}";
    '''
    resp = requests.post(url, json={'query': query})

    # Check for response errors
    if resp.status_code != 200:
        return jsonify({"error": "Failed to fetch data from the API"}), resp.status_code

    # response
    data = resp.json()
    if 'data' in data and data['data']:
        return jsonify({'summary': data['data'][0][0]})
    else:
        return jsonify({'error': 'No summary found'}), 404

@app.route("/qa")
def answer_question():
    text = request.args.get('text', '')
    question = request.args.get('question', '')

    if not question or not text:
        return jsonify({"error": "Both 'text' and 'question' parameters are required"}), 400
    
    # connect
    url = 'http://127.0.0.1:47334/api/sql/query'

    # query
    query = f'''
    SELECT * FROM google_gemini_model WHERE question = "Answer the following question: '{question}' based on the text: '{text}'";
    '''
    resp = requests.post(url, json={'query': query})

    # Check for response errors
    if resp.status_code != 200:
        return jsonify({"error": "Failed to fetch data from the API"}), resp.status_code

    # Extract and return the answer from the response
    data = resp.json()
    if 'data' in data and data['data']:
        return jsonify({'answer': data['data'][0][0]})
    else:
        return jsonify({'error': 'No answer found'}), 404

if __name__ == "__main__":
    app.run(debug=True)
