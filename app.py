from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)
attempts = 0
MAX_ATTEMPTS = 7

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    global attempts, secret_number

    data = request.json
    number = int(data["number"])
    attempts += 1

    if number == secret_number:
        return jsonify(
            message="🎉 Chính xác! Anh đoán đúng rồi!",
            status="win"
        )

    if attempts >= MAX_ATTEMPTS:
        answer = secret_number
        secret_number = random.randint(1, 100)
        attempts = 0
        return jsonify(
            message=f"💀 Hết lượt! Số đúng là {answer}",
            status="lose"
        )

    if number < secret_number:
        return jsonify(
            message=f"Số cần tìm LỚN hơn ({attempts}/{MAX_ATTEMPTS})",
            status="continue"
        )
    else:
        return jsonify(
            message=f"Số cần tìm NHỎ hơn ({attempts}/{MAX_ATTEMPTS})",
            status="continue"
        )

@app.route("/reset", methods=["POST"])
def reset():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    return jsonify(message="🔄 Game đã được reset")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
