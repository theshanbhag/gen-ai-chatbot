import vertexai
from flask import Flask, request, render_template, redirect

import chatter

app = Flask(__name__)

chat_model, parameters = chatter.predict_large_language_model_sample("gcp-pov", "chat-bison@001", 0.8, 100, 0.8, 40,
                                                                  "us-central1")
chat = chat_model.start_chat(
        context='''
        You are a Customer support agent with name Sara. 
        You should reply "I am Sara" for "Hi".
        XYZ has a product named Aabaa and Baabaa.
        Aabaa is a primary product and Beta is back up product.
        Aabaa has 10 features and Baabaa has 5 features.''',
        examples=[]
    )

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route('/chat', methods=["GET", "POST"])
def chat_with_ai():
    question = request.form['question']
    response = chatter.chat_with_model(chat_model, parameters, question, chat)
    return response


app.run(host='0.0.0.0', port=81, debug=True)
