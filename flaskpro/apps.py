from flask import Flask, render_template, request, jsonify
from rasa.core.agent import Agent

app = Flask(__name__)

rasa_model = Agent.load(r"C:\Users\Subhasri\Desktop\punchbiz-2\punchbiz\models\20240303-190752-burning-arrowroot.tar.gz")

@app.route('/health')
def health_check():
    return 'Frontend is connected to the backend.'

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
async def send_message():
    user_message = request.json.get('message')
    response = await rasa_model.handle_text(user_message)
    bot_response = response[0]['text'] if response else "Sorry, I didn't understand that."
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
