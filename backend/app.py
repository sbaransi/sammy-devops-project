from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Sammy DevOps Shop API"})

@app.route("/products")
def get_products():

    conn = psycopg2.connect(
        host="postgres",
        database="sammyshop",
        user="sammy",
        password="secret123"
    )

    cur = conn.cursor()

    cur.execute("SELECT id, name FROM products")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    products = []

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1]
        })

    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)