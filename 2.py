from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Yhteys tietokantaan
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="",
    autocommit=True
)

@app.route("/kentta/<icao>", methods=["GET"])
def get_airport(icao):

    sql = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """

    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        response = {
            "ICAO": result[0],
            "Name": result[1],
            "Municipality": result[2]
        }
    else:
        response = {
            "error": "Airport not found"
        }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)