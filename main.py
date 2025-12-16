from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import crud as cd


app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/')
def index():
    return render_template("frontend.html")

@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()

    if not data or "task" not in data or not data["task"].strip():
        return jsonify({"message": "Task is required"}), 400

    cd.create_todo(data["task"].strip())
    return jsonify({"message": "Todo created"}), 201

@app.route("/todos", methods=["GET"])
def get_todos():
    tasks = cd.load_tasks()
    result = []

    for task in tasks:
        id_, task_name, task_date, is_done = task
        result.append({
            "id": id_,
            "task": task_name,
            "date": task_date.strftime("%Y-%m-%d"),
            "done": bool(is_done)
        })
    return jsonify(result), 200

@app.route("/todos/<int:task_id>", methods=["PUT"])
def update_todo(task_id):
    affected = cd.update_task_done(task_id)

    if affected == 0:
        return jsonify({"message": "Todo not found"}), 404

    return jsonify({"message": "Todo updated"}), 200


@app.route("/todos/<int:task_id>", methods=["DELETE"])
def delete_todo(task_id):
    affected = cd.delete_tasks(task_id)

    if affected == 0:
        return jsonify({"message": "Todo not found"}), 404

    return "", 204


@app.route("/todos/reset", methods=["POST"])
def reset_ids():
    cd.reset_auto_increment()
    return jsonify({"message": "Auto increment reset"}), 200

if __name__ == "__main__":
    app.run(debug=True)