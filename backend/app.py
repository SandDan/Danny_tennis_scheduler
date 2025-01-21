# import Flask other dependencies, Flask core framework,request handles HTTP requests, jsonify returns JSON responses

from flask import Flask, request, jsonify

#Flask App instance, entry point
app = Flask(__name__)

#Purpose: Home Route
#define URLS app responds to, / = root URL, def home(): = function that runs whenever root is visited.
@app.route('/')
def home():
    return "Welcome to the Tennis Lesson Scheduler"

#Purpose: Fetch available lessons
#methods=['GET']: sepecifies HTTP method get
#jsonify(): converts Python objects (such as list or dict) to JSON format 
@app.route("/api/lessons", methods=['GET'])
def get_lessons():
    lessons = [
        {"id": 1, "date": "2025-01-22", "time": "09:00", "available": True},
        {"id": 2, "date": "2025-01-22", "time": "10:00", "available": False},
    ]
    return jsonify(lessons)

#Handles lesson bookings
#request.json 
#Response: returns success mesage with a 201 status code
@app.route('/api/book', methods=['POST'])
def book_lesson():
    data = request.json #Parse JSON payload from the client
    lesson_id = data.get('lesson_id')
    user_name = data.get('user_name')
    user_email = data.get('user_email')

    #Example logic, TODO replace with database 
    return jsonify({
        "message": f"Lesson {lesson_id} booked successfully for {user_name}.",
        "status": "success"
    }), 201

#Purpose: Runs the app
if __name__ == "__main__":
    app.run(debug=True)