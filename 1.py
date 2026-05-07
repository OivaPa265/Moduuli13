from flask import Flask, jsonify

app = Flask(__name__)

def onalku(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


@app.route("/alkuluku/<int:number>", methods=["GET"])
def alkuluku(number):
    result = {
        "numero": number,
        "onalku": onalku(number)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)