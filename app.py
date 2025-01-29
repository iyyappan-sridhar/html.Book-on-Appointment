from flask import Flask, request, jsonify

app = Flask(__name__)

# This will store appointment data temporarily in memory.
appointments = []

@app.route('/')
def index():
    return "Psychologist Appointment Booking API"

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    try:
        # Get appointment data from the request
        data = request.get_json()
        name = data['name']
        email = data['email']
        date = data['date']
        time = data['time']

        # Store the appointment (in a real app, this should go to a database)
        appointment = {
            'name': name,
            'email': email,
            'date': date,
            'time': time
        }
        appointments.append(appointment)

        return jsonify({'message': 'Your appointment has been successfully booked!'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to book appointment. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
