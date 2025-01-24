from flask import Flask, render_template, request, jsonify
from chatbot import get_response

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")  # Home page with chat UI

    @app.route("/chat", methods=["POST"])
    def chat():
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"error": "No input provided"}), 400
        
        # Get chatbot response
        response = get_response(user_input)
        return jsonify({"response": response})

    return app
