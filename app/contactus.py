from flask import Flask,jsonify,request
from datetime import datetime

app =Flask(__name__)
file_path = 'contact.txt'

@app.route('/api/contact',methods=['GET'])
def get_contacts():
    try:
        # Appending content to the file
        name = request.args.get('name', 'Guest')
        email = request.args.get('email', 'Not specified')
        subject = request.args.get('subject', 'Unknown')
        phone = request.args.get('phone', 'Unknown')
        message = request.args.get('message', 'Unknown')
        # Get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, 'a') as file:
            file.write(f'Date and Time: {current_datetime}\n')
            file.write(f'Name: {name}\n')
            file.write(f'Email: {email}\n')
            file.write(f'Subject: {subject}\n')
            file.write(f'Phone: {phone}\n')
            file.write(f'Message: {message}\n\n')
        return jsonify({'success': True}), 200
    except Exception as e:
         # Handle any exceptions and respond with an error message
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)