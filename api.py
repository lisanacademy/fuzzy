from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/fuzzy")
def fuzzy():
    score = float(request.args.get("score",0))

    if score > 80:
        result="High"
    elif score > 50:
        result="Medium"
    else:
        result="Low"

    return jsonify({"result":result})