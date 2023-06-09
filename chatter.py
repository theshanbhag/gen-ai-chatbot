import vertexai
from vertexai.preview.language_models import ChatModel


def predict_large_language_model_sample(
        project_id: str,
        model_name: str,
        temperature: float,
        max_output_tokens: int,
        top_p: float,
        top_k: int,
        location: str = "us-central1",
):
    """Predict using a Large Language Model."""
    vertexai.init(project=project_id, location=location)
    chat_model = ChatModel.from_pretrained(model_name)
    parameters = {
        "temperature": temperature,
        "max_output_tokens": max_output_tokens,
        "top_p": top_p,
        "top_k": top_k,
    }
    return chat_model, parameters


def chat_with_model(parameters, question, chat):
    conversation = {"question": question}
    response = chat.send_message(question, **parameters)
    print(response.text)
    conversation["response"] = response.text
    return response.text, conversation


def connect_cluster():
    import pymongo
    client = pymongo.MongoClient(
        "mongodb+srv://venkatesh:ashwin123@freetier.kxcgwh2.mongodb.net/?retryWrites=true&w=majority",
        tlsAllowInvalidCertificates=True)
    return client


def query_db(client, db_name, col_name, doc):
    db = client[db_name]
    col = db[col_name]
    x = col.find_one(doc)
    return x


def upsert_db(client, db_name, col_name, doc, customer_id):
    db = client[db_name]
    col = db[col_name]
    col.update_one({"customer_id": customer_id}, {"$push": {"conversation": doc}})
