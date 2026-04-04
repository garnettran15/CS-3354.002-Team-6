#Keerthan Sanjay
# ==========================================
# MODULE: Server Logic
# This file starts the website and manages the data.
# ==========================================

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# This dictionary stores the user's information while the app is running.
user_data = {
    "weight": "185 lbs",
    "height": "6'0",
    "goal": "Maintain Muscle & Lose Body Fat"
}

# MODULE: Dashboard Route (UC-04)
# This function loads the main dashboard page.
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# MODULE: Profile Route (UC-03)
# This function loads the profile page and fills in the current user data.
@app.route('/profile')
def profile():
    return render_template('profile.html', data=user_data)

# MODULE: Update Handler
# This function receives new information from the profile page.
@app.route('/api/update', methods=['POST'])
def update_profile():
    new_info = request.json
    
    # TEST CASE 2: Check for empty input.
    # If the weight box is empty, stop the update and send an error.
    if not new_info.get('weight') or new_info.get('weight').strip() == "":
        return jsonify({"message": "Error: Weight cannot be empty!"}), 400
    
    # TEST CASE 1: Successful update.
    # If the input is valid, save the new data and send a success message.
    user_data.update(new_info)
    return jsonify({"message": "Dietary profile updated successfully!"})

if __name__ == '__main__':
    app.run(debug=True)