# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle form submission here (e.g., store the data in a database)
        # For simplicity, we'll just print the submitted data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        print(f"First Name: {first_name}, Last Name: {last_name}, Email: {email}")

        return "Registration successful!"

    return render_template('register_form.html')

if __name__ == '__main__':
    app.run(debug=True)
