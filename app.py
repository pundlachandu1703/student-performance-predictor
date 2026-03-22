from flask import Flask, render_template, request

# Initialize Flask App
app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')


# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        study_hours = float(request.form['study_hours'])
        attendance = float(request.form['attendance'])
        marks = float(request.form['marks'])

        # Score Calculation
        score = (study_hours * 5) + (attendance * 0.3) + (marks * 0.5)

        # Performance Logic
        if score >= 80:
            result = "🌟 Excellent Performance"
            color = "green"
            description = "You are performing very well academically. Your consistency in studies and good attendance are clearly reflected in your marks."
            tips = "Keep maintaining this level! Try advanced learning, participate in competitions, and help others."

        elif score >= 50:
            result = "👍 Average Performance"
            color = "orange"
            description = "Your performance is decent but there is room for improvement. A bit more focus and consistency can boost your results."
            tips = "Increase study time, revise daily, and focus on weak subjects. Practice previous papers regularly."

        else:
            result = "⚠️ Poor Performance"
            color = "red"
            description = "Your current performance is below expectations. Low study hours or attendance may be affecting your marks."
            tips = "Create a proper study schedule, attend classes regularly, and focus on basic concepts. Avoid distractions."

        return render_template(
            'index.html',
            prediction=result,
            color=color,
            description=description,
            tips=tips
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction="Error: Please enter valid inputs",
            color="red",
            description=str(e),
            tips="Check your inputs and try again."
        )


# Run App
if __name__ == "__main__":
    app.run(debug=True)