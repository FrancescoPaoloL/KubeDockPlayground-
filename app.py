from flask import Flask, request, abort, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
    try:
        data = request.get_json()
        value1, value2 = data.get('value1'), data.get('value2')

        if value1 is not None and value2 is not None:
            try:
                value1 = float(value1)
                value2 = float(value2)

                result = value1 + value2

                response = jsonify(result=result)  # Convert result to JSON format
                return response
            except ValueError:
                abort(400, jsonify(error="Please enter valid numbers."))
        else:
            abort(400, jsonify(error="Please provide both 'value1' and 'value2' in the request body."))
    except HTTPException as e:
        response = jsonify(error=str(e))
        response.status_code = e.code
        return response

if __name__ == '__main__':
    print("This is a simple web service that accepts two numbers and returns their sum.\n"
          "You can send a POST request with parameters 'value1' and 'value2' to http://localhost:8080.\n")
    app.run(host="0.0.0.0", port=8080)

