from flask import Blueprint, request, jsonify
from database import get_connection


flavors_bp = Blueprint("flavors", __name__)

@flavors_bp.route("/flavors", methods=["GET", "POST"])
def manage_flavors():
    conn = get_connection()
    if request.method == "POST":
        data = request.json
        conn.execute("INSERT INTO Flavors (name, season, price) VALUES (?, ?, ?)",
                     (data["name"], data["season"], data["price"]))
        conn.commit()
        return jsonify({"message": "Flavor added successfully"}), 201
    flavors = conn.execute("SELECT * FROM Flavors").fetchall()
    return jsonify([dict(row) for row in flavors])
