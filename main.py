from flask import Flask, request
import requests
import os

app = Flask(__name__)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.route("/")
def home():
    return "Bot está online!", 200

    @app.route("/webhook", methods=["POST"])
    def webhook():
        if request.method == "POST":
                data = request.get_json()

chat_id = dados["mensagem"]["chat"]["id"]
                                text = data["message"]["text"]

                                        resposta = f"Você disse: {text}"
                                                enviar_mensagem(chat_id, resposta)
                                                        return "ok", 200

                                                        def enviar_mensagem(chat_id, texto):
                                                            url = f"{URL}/sendMessage"
                                                                payload = {
                                                                        "chat_id": chat_id,
                                                                                "text": texto
                                                                                    }
                                                                                        requests.post(url, json=payload)

                                                                                        if __name__ == "__main__":
                                                                                            port = int(os.environ.get("PORT", 5000))
                                                                                                app.run(host="0.0.0.0", port=port)
                                                                                            