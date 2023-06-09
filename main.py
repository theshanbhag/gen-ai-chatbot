from flask import Flask, request, render_template

import chatter
from vertexai.preview.language_models import InputOutputTextPair
conversation = []

app = Flask(__name__)

conn = chatter.connect_cluster()
intro_context = chatter.query_db(conn, "XYZ-Corp", "Insurance", {"type": "Intro"})
saved_conversation = chatter.query_db(conn, "XYZ-Corp", "Customer", {"customer_id": "123"})

context = intro_context["context"]
chat_model, parameters = chatter.predict_large_language_model_sample("gcp-pov", "chat-bison@001", 0.8, 100, 0.8, 40,
                                                                     "us-central1")
try:
    if saved_conversation != {}:
        for i in saved_conversation["conversation"]:
            conversation.append(
                InputOutputTextPair(
                    input_text=i["question"],
                    output_text=i["response"]
                )
            )
except Exception as e:
    conversation = []

print(conversation)
chat = chat_model.start_chat(
    context=context,
    examples=conversation
)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route('/chat', methods=["GET", "POST"])
def chat_with_ai():
    question = request.form['question']
    response_text, conversation = chatter.chat_with_model(parameters, question, chat)
    chatter.upsert_db(conn, "XYZ-Corp", "Customer", conversation, "123")
    return response_text


app.run(host='0.0.0.0', port=81, debug=True)
